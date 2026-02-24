import gc
import json
import logging
import os
import resource
import signal
import threading
import time
import weakref
from collections import defaultdict, deque
from datetime import datetime, timezone
from typing import Any

try:
    import psutil
except Exception:  # pragma: no cover
    psutil = None

try:
    import tracemalloc
except Exception:  # pragma: no cover
    tracemalloc = None

logger = logging.getLogger("memdiag")


_TRACE_FOCUS_DEFAULTS = (
    "flet/controls/object_patch.py",
    "flet/components/component.py",
    "flet/messaging/session.py",
)


def _env_bool(name: str, default: bool = False) -> bool:
    value = os.getenv(name)
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "yes", "on"}


def _env_int(name: str, default: int) -> int:
    raw = os.getenv(name)
    if raw is None:
        return default
    try:
        return int(raw)
    except ValueError:
        return default


def _env_csv(name: str, default: tuple[str, ...]) -> tuple[str, ...]:
    value = os.getenv(name)
    if value is None:
        return default
    items = [part.strip() for part in value.split(",") if part.strip()]
    return tuple(items) if items else default


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def _parse_iso_utc(ts: str) -> datetime:
    return datetime.fromisoformat(ts)


def _is_control_instance(obj: Any) -> bool:
    # Flet controls/components expose internal control metadata as `_c` + `_i`.
    # Some wrappers may also expose `_get_control_name`.
    return (hasattr(obj, "_c") and hasattr(obj, "_i")) or hasattr(
        obj, "_get_control_name"
    )


def _iter_possible_controls(value: Any):
    if _is_control_instance(value):
        yield value
        return

    if isinstance(value, (list, tuple, set)):
        for item in value:
            yield from _iter_possible_controls(item)
        return

    if isinstance(value, dict):
        for item in value.values():
            yield from _iter_possible_controls(item)


def _iter_control_children(control: Any):
    # Flet Component wrappers render actual controls into `_b`.
    body = getattr(control, "_b", None)
    if body is not None:
        yield from _iter_possible_controls(body)

    # Fast path for common control containers.
    for attr in ("content", "controls", "views", "leading", "trailing"):
        value = getattr(control, attr, None)
        if value is not None:
            yield from _iter_possible_controls(value)

    # Fallback: inspect all dataclass/object fields.
    try:
        control_values = vars(control).values()
    except TypeError:
        control_values = ()

    for value in control_values:
        yield from _iter_possible_controls(value)


class MemoryDiagnostics:
    def __init__(self) -> None:
        self.enabled = _env_bool("MEM_DIAG", False)
        self.interval_sec = max(10, _env_int("MEM_DIAG_INTERVAL_SEC", 60))
        self.trace_interval_sec = max(60, _env_int("MEM_DIAG_TRACE_INTERVAL_SEC", 600))
        self.trace_frames = max(1, _env_int("MEM_DIAG_TRACE_FRAMES", 10))
        self.trace_top = max(1, _env_int("MEM_DIAG_TRACE_TOP", 20))
        self.trace_focus_files = _env_csv(
            "MEM_DIAG_TRACE_FOCUS_FILES", _TRACE_FOCUS_DEFAULTS
        )
        self.control_scan_max_nodes = max(1000, _env_int("MEM_DIAG_CONTROL_SCAN_MAX_NODES", 10000))
        self.collect_on_sample = _env_bool("MEM_DIAG_COLLECT_ON_SAMPLE", False)
        self.collect_gen2_on_sample = _env_bool("MEM_DIAG_COLLECT_GEN2_ON_SAMPLE", True)
        self.control_scan_enabled = _env_bool("MEM_DIAG_CONTROL_SCAN", False)
        self.gc_objects_enabled = _env_bool("MEM_DIAG_GC_OBJECTS", False)
        self.type_hist_enabled = _env_bool("MEM_DIAG_TYPE_HIST", False)
        self.type_hist_interval_sec = max(
            60, _env_int("MEM_DIAG_TYPE_HIST_INTERVAL_SEC", 900)
        )
        self.type_hist_top = max(5, _env_int("MEM_DIAG_TYPE_HIST_TOP", 30))

        self._lock = threading.Lock()
        self._started = False
        self._thread: threading.Thread | None = None
        self._pages = weakref.WeakSet()
        self._active_pages = weakref.WeakSet()
        self._control_types: dict[str, weakref.WeakSet] = defaultdict(weakref.WeakSet)

        self._sessions_started = 0
        self._sessions_disconnected = 0

        self._samples = deque(maxlen=500)
        self._events = deque(maxlen=500)
        self._trace_reports = deque(maxlen=100)

        self._proc = psutil.Process(os.getpid()) if psutil else None
        self._last_trace_ts = 0.0
        self._last_snapshot = None
        self._last_type_hist_ts = 0.0
        self._last_type_hist_counts: dict[str, int] = {}
        self._type_hist_reports = deque(maxlen=100)

    def enable_for_page(self, page: Any) -> None:
        if not self.enabled:
            return

        with self._lock:
            self._sessions_started += 1
            self._pages.add(page)
            self._active_pages.add(page)
            page_id = self._page_id(page)
            self._events.append(
                {
                    "ts": _now_iso(),
                    "event": "session_start",
                    "page_id": page_id,
                    "route": getattr(page, "route", None),
                }
            )

        self._attach_page_handlers(page)
        self._ensure_started()

    def dump_now(self, reason: str = "manual") -> dict[str, Any]:
        if not self.enabled:
            return {"enabled": False}

        payload = {
            "ts": _now_iso(),
            "reason": reason,
            "summary": self._collect_summary(),
            "summary_trends": self._summarize_recent_trends(),
            "recent_samples": list(self._samples)[-10:],
            "recent_events": list(self._events)[-20:],
            "recent_tracemalloc": list(self._trace_reports)[-5:],
            "recent_type_hist": list(self._type_hist_reports)[-5:],
        }
        logger.info("[mem_diag_dump] %s", json.dumps(payload, default=str))
        return payload

    def _ensure_started(self) -> None:
        with self._lock:
            if self._started:
                return
            self._started = True

            if tracemalloc is not None:
                tracemalloc.start(self.trace_frames)
                self._last_snapshot = tracemalloc.take_snapshot()
                self._last_trace_ts = time.time()

            gc.callbacks.append(self._gc_callback)
            self._install_signal_handler()

            self._thread = threading.Thread(target=self._sampler_loop, daemon=True)
            self._thread.start()

            logger.info(
                "Memory diagnostics enabled: interval=%ss trace_interval=%ss",
                self.interval_sec,
                self.trace_interval_sec,
            )

    def _attach_page_handlers(self, page: Any) -> None:
        previous_connect = getattr(page, "on_connect", None)
        previous_disconnect = getattr(page, "on_disconnect", None)

        def on_connect(e):
            with self._lock:
                self._active_pages.add(page)
                self._events.append(
                    {
                        "ts": _now_iso(),
                        "event": "page_connect",
                        "page_id": self._page_id(page),
                        "route": getattr(page, "route", None),
                    }
                )
            if callable(previous_connect):
                previous_connect(e)

        def on_disconnect(e):
            with self._lock:
                try:
                    self._active_pages.remove(page)
                except KeyError:
                    pass
                self._sessions_disconnected += 1
                self._events.append(
                    {
                        "ts": _now_iso(),
                        "event": "page_disconnect",
                        "page_id": self._page_id(page),
                        "route": getattr(page, "route", None),
                    }
                )
            if callable(previous_disconnect):
                previous_disconnect(e)

        page.on_connect = on_connect
        page.on_disconnect = on_disconnect

    def _page_id(self, page: Any) -> str:
        session_id = getattr(page, "session_id", None)
        return str(session_id if session_id is not None else id(page))

    def _sampler_loop(self) -> None:
        while True:
            time.sleep(self.interval_sec)
            try:
                self._sample_once()
            except Exception:
                logger.exception("mem_diag sampler failed")

    def _sample_once(self) -> None:
        gc_collect = None
        if self.collect_on_sample:
            gc_generation = 2 if self.collect_gen2_on_sample else None
            gc_collected = gc.collect(2) if self.collect_gen2_on_sample else gc.collect()
            gc_collect = {
                "generation": gc_generation,
                "collected": gc_collected,
                "garbage_len": len(gc.garbage),
                "gc_counts_after": gc.get_count(),
            }

        scan_stats = (
            self._scan_page_controls()
            if self.control_scan_enabled
            else {"scanned_nodes": 0, "unique_objects": 0, "truncated": 0}
        )
        summary = self._collect_summary()
        try:
            session_stats = self._collect_session_stats()
        except Exception as ex:
            session_stats = {
                "sessions_reachable": 0,
                "sessions_active_reachable": 0,
                "session_control_index_total": 0,
                "session_control_index_max": 0,
                "session_control_index_avg": 0.0,
                "active_session_control_index_total": 0,
                "active_session_control_index_max": 0,
                "active_session_control_index_avg": 0.0,
                "error": f"{type(ex).__name__}: {ex}",
            }
            self._events.append(
                {
                    "ts": _now_iso(),
                    "event": "mem_diag_warning",
                    "where": "_collect_session_stats",
                    "error": f"{type(ex).__name__}: {ex}",
                }
            )
        gc_objects = len(gc.get_objects()) if self.gc_objects_enabled else None
        sample = {
            "ts": _now_iso(),
            "rss_bytes": self._rss_bytes(),
            "gc_counts": gc.get_count(),
            "gc_objects": gc_objects,
            "gc_collect": gc_collect,
            "sessions_started": summary["sessions_started"],
            "sessions_disconnected": summary["sessions_disconnected"],
            "pages_seen": summary["pages_seen"],
            "pages_active": summary["pages_active"],
            "control_type_counts": summary["control_type_counts"],
            "session_stats": session_stats,
            "control_scan": scan_stats,
        }
        self._samples.append(sample)

        maybe_trace = self._capture_trace_growth()
        if maybe_trace:
            self._trace_reports.append(maybe_trace)
        maybe_type_hist = self._capture_type_hist()
        if maybe_type_hist:
            self._type_hist_reports.append(maybe_type_hist)
            sample["type_hist"] = maybe_type_hist

        logger.info("[mem_diag_sample] %s", json.dumps(sample, default=str))
        if maybe_trace:
            logger.info("[mem_diag_trace] %s", json.dumps(maybe_trace, default=str))
        if maybe_type_hist:
            logger.info("[mem_diag_type_hist] %s", json.dumps(maybe_type_hist, default=str))

    def _collect_summary(self) -> dict[str, Any]:
        with self._lock:
            return {
                "sessions_started": self._sessions_started,
                "sessions_disconnected": self._sessions_disconnected,
                "pages_seen": len(self._pages),
                "pages_active": len(self._active_pages),
                "control_type_counts": {
                    name: len(refs)
                    for name, refs in sorted(
                        self._control_types.items(), key=lambda item: len(item[1]), reverse=True
                    )[:20]
                },
            }

    def _collect_session_stats(self) -> dict[str, Any]:
        with self._lock:
            pages_snapshot = list(self._pages)
            active_snapshot = set(self._active_pages)

        sessions_all: dict[int, Any] = {}
        sessions_active: dict[int, Any] = {}

        for page in pages_snapshot:
            sess = self._resolve_page_session(page)
            if sess is None:
                continue
            sid = id(sess)
            sessions_all[sid] = sess
            if page in active_snapshot:
                sessions_active[sid] = sess

        all_sizes = [self._session_index_size(s) for s in sessions_all.values()]
        active_sizes = [self._session_index_size(s) for s in sessions_active.values()]

        return {
            "sessions_reachable": len(sessions_all),
            "sessions_active_reachable": len(sessions_active),
            "session_control_index_total": sum(all_sizes),
            "session_control_index_max": max(all_sizes) if all_sizes else 0,
            "session_control_index_avg": (sum(all_sizes) / len(all_sizes)) if all_sizes else 0,
            "active_session_control_index_total": sum(active_sizes),
            "active_session_control_index_max": max(active_sizes) if active_sizes else 0,
            "active_session_control_index_avg": (sum(active_sizes) / len(active_sizes)) if active_sizes else 0,
        }

    def _resolve_page_session(self, page: Any) -> Any:
        # Prefer private backing storage to avoid calling page.session property
        # on pages whose session weakref has already been cleared.
        try:
            page_vars = vars(page)
        except Exception:
            page_vars = {}

        session_ref = page_vars.get("_Page__session")
        if callable(session_ref):
            try:
                sess = session_ref()
            except Exception:
                sess = None
            if sess is not None:
                return sess

        for attr_name in ("_session", "sess"):
            sess = self._safe_getattr(page, attr_name, None)
            if sess is not None:
                return sess

        # Last resort: guarded access to property-based API.
        return self._safe_getattr(page, "session", None)

    @staticmethod
    def _safe_getattr(obj: Any, name: str, default: Any = None) -> Any:
        try:
            return getattr(obj, name)
        except Exception:
            return default

    def _session_index_size(self, session: Any) -> int:
        for attr_name in ("index", "_Session__index", "_index", "controls_index"):
            index = self._safe_getattr(session, attr_name, None)
            if index is None:
                continue
            try:
                return len(index)
            except Exception:
                pass

        # Fallback for runtime variants with different private names.
        try:
            data = vars(session)
        except Exception:
            data = {}
        for key, value in data.items():
            if "index" not in key:
                continue
            try:
                return len(value)
            except Exception:
                continue
        return 0

    def _summarize_recent_trends(self) -> dict[str, Any]:
        samples = list(self._samples)
        if len(samples) < 2:
            return {}

        first = samples[0]
        last = samples[-1]
        try:
            dt_sec = max((_parse_iso_utc(last["ts"]) - _parse_iso_utc(first["ts"])).total_seconds(), 1.0)
        except Exception:
            dt_sec = 1.0

        pages_first = max(1, int(first.get("pages_active") or 0))
        pages_last = max(1, int(last.get("pages_active") or 0))

        rss_first = first.get("rss_bytes")
        rss_last = last.get("rss_bytes")

        ctrl_first = int(first.get("control_scan", {}).get("scanned_nodes") or 0)
        ctrl_last = int(last.get("control_scan", {}).get("scanned_nodes") or 0)

        comp_first = int((first.get("control_type_counts") or {}).get("Component", 0))
        comp_last = int((last.get("control_type_counts") or {}).get("Component", 0))

        tuple_first = self._type_count_in_sample(first, "builtins.tuple")
        tuple_last = self._type_count_in_sample(last, "builtins.tuple")

        summary = {
            "window_seconds": dt_sec,
            "sample_count": len(samples),
            "pages_active": {"first": pages_first, "last": pages_last, "delta": pages_last - pages_first},
            "controls_per_active_page": {
                "first": ctrl_first / pages_first,
                "last": ctrl_last / pages_last,
                "delta": (ctrl_last / pages_last) - (ctrl_first / pages_first),
            },
            "components_per_active_page": {
                "first": comp_first / pages_first,
                "last": comp_last / pages_last,
                "delta": (comp_last / pages_last) - (comp_first / pages_first),
            },
        }

        if rss_first is not None and rss_last is not None:
            summary["rss_bytes"] = {
                "first": rss_first,
                "last": rss_last,
                "delta": rss_last - rss_first,
                "delta_per_min": (rss_last - rss_first) * 60.0 / dt_sec,
            }
            summary["rss_bytes_per_active_page"] = {
                "first": rss_first / pages_first,
                "last": rss_last / pages_last,
                "delta": (rss_last / pages_last) - (rss_first / pages_first),
            }

        if tuple_first is not None and tuple_last is not None:
            summary["tuple_count_per_active_page"] = {
                "first": tuple_first / pages_first,
                "last": tuple_last / pages_last,
                "delta": (tuple_last / pages_last) - (tuple_first / pages_first),
                "abs_delta": tuple_last - tuple_first,
            }

        return summary

    def _type_count_in_sample(self, sample: dict[str, Any], type_name: str) -> int | None:
        type_hist = sample.get("type_hist")
        if not isinstance(type_hist, dict):
            return None
        for entry in type_hist.get("top_types", []):
            if entry.get("type") == type_name:
                return int(entry.get("count", 0))
        return None

    def _scan_page_controls(self) -> dict[str, int]:
        scanned_nodes = 0
        seen = set()

        with self._lock:
            pages_snapshot = list(self._pages)

        for page in pages_snapshot:
            try:
                roots_obj = getattr(page, "views", None)
            except Exception:
                # Some runtime versions expose page.views via a property
                # that may fail while the page is mutating.
                roots_obj = None

            if roots_obj is None:
                roots = []
            elif isinstance(roots_obj, (list, tuple, set)):
                roots = list(roots_obj)
            else:
                try:
                    roots = list(roots_obj)
                except TypeError:
                    roots = [roots_obj]

            stack = roots

            while stack and scanned_nodes < self.control_scan_max_nodes:
                control = stack.pop()
                cid = id(control)
                if cid in seen:
                    continue
                seen.add(cid)

                if not _is_control_instance(control):
                    continue

                scanned_nodes += 1
                control_type = control.__class__.__name__
                try:
                    self._control_types[control_type].add(control)
                except TypeError:
                    pass

                for child in _iter_control_children(control):
                    stack.append(child)

            if scanned_nodes >= self.control_scan_max_nodes:
                break

        return {
            "scanned_nodes": scanned_nodes,
            "unique_objects": len(seen),
            "truncated": int(scanned_nodes >= self.control_scan_max_nodes),
        }

    def _capture_trace_growth(self) -> dict[str, Any] | None:
        if tracemalloc is None or self._last_snapshot is None:
            return None

        now = time.time()
        if now - self._last_trace_ts < self.trace_interval_sec:
            return None

        current_snapshot = tracemalloc.take_snapshot()
        diffs = current_snapshot.compare_to(self._last_snapshot, "lineno")
        self._last_snapshot = current_snapshot
        self._last_trace_ts = now

        top = []
        focus = []
        for stat in diffs:
            if not stat.traceback:
                continue
            frame = stat.traceback[0]
            row = {
                "file": frame.filename,
                "line": frame.lineno,
                "size_diff_bytes": stat.size_diff,
                "count_diff": stat.count_diff,
            }
            if len(top) < self.trace_top:
                top.append(row)
            if self._is_trace_focus_file(frame.filename):
                focus.append(row)
                if len(focus) >= self.trace_top:
                    pass
            if len(top) >= self.trace_top and len(focus) >= self.trace_top:
                break

        return {
            "ts": _now_iso(),
            "trace_focus_files": self.trace_focus_files,
            "top_growth": top,
            "top_growth_focus": focus,
        }

    def _is_trace_focus_file(self, filename: str) -> bool:
        for suffix in self.trace_focus_files:
            if filename.endswith(suffix):
                return True
        return False

    def _capture_type_hist(self) -> dict[str, Any] | None:
        if not self.type_hist_enabled:
            return None

        now = time.time()
        if now - self._last_type_hist_ts < self.type_hist_interval_sec:
            return None

        counts: dict[str, int] = defaultdict(int)
        try:
            objects = gc.get_objects()
        except Exception:
            return None

        for obj in objects:
            t = type(obj)
            type_name = f"{t.__module__}.{t.__name__}"
            counts[type_name] += 1

        top_counts = sorted(counts.items(), key=lambda item: item[1], reverse=True)[
            : self.type_hist_top
        ]
        top = [{"type": name, "count": count} for name, count in top_counts]

        deltas = []
        for name, count in top_counts:
            prev = self._last_type_hist_counts.get(name, 0)
            delta = count - prev
            if delta != 0:
                deltas.append({"type": name, "delta": delta, "count": count})

        deltas.sort(key=lambda item: abs(item["delta"]), reverse=True)

        self._last_type_hist_counts = dict(counts)
        self._last_type_hist_ts = now

        return {
            "ts": _now_iso(),
            "top_types": top,
            "top_deltas": deltas[: self.type_hist_top],
        }

    def _gc_callback(self, phase: str, info: dict[str, Any]) -> None:
        if phase != "stop":
            return

        self._events.append(
            {
                "ts": _now_iso(),
                "event": "gc_stop",
                "generation": info.get("generation"),
                "collected": info.get("collected"),
                "uncollectable": info.get("uncollectable"),
                "gc_counts": gc.get_count(),
            }
        )

    def _rss_bytes(self) -> int | None:
        if self._proc is not None:
            try:
                return int(self._proc.memory_info().rss)
            except Exception:
                pass

        # Fallback when psutil is unavailable. ru_maxrss semantics differ by OS.
        # On macOS this value is already in bytes; on Linux it is in KiB.
        try:
            rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
            if os.name == "posix" and os.uname().sysname == "Linux":
                return int(rss * 1024)
            return int(rss)
        except Exception:
            return None

    def _install_signal_handler(self) -> None:
        if not hasattr(signal, "SIGUSR1"):
            return

        def handle_sigusr1(_signum, _frame):
            self.dump_now(reason="sigusr1")

        try:
            signal.signal(signal.SIGUSR1, handle_sigusr1)
        except Exception:
            logger.warning("Could not install SIGUSR1 handler for mem diagnostics")


diagnostics = MemoryDiagnostics()
