import gc
import logging
import threading
import time
import tracemalloc

import flet as ft
import objgraph

from components.app import App
from models.gallery import Gallery


def start_mem_watch(interval_s=60):
    tracemalloc.start(25)
    gc.collect()
    baseline = tracemalloc.take_snapshot()

    def loop():
        nonlocal baseline
        while True:
            time.sleep(interval_s)
            gc.collect()
            snap = tracemalloc.take_snapshot()
            top = snap.compare_to(baseline, "lineno")

            print("\n[mem_watch] Top growth since baseline:")
            for stat in top[:15]:
                print(stat)

            # optional: reset baseline so growth is per-interval
            baseline = snap

    t = threading.Thread(target=loop, daemon=True)
    t.start()


def start_gc_watch(interval_s=60):
    gc.set_debug(gc.DEBUG_STATS)

    def loop():
        while True:
            time.sleep(interval_s)
            gc.collect()
            print("\n[gc_watch] Object growth (since last call):")
            objgraph.show_growth(limit=20)

    t = threading.Thread(target=loop, daemon=True)
    t.start()


logging.basicConfig(level=logging.INFO)


gallery = Gallery()

if __name__ == "__main__":
    # start_gc_watch(60)
    ft.run(lambda page: page.render_views(lambda: App(gallery)))
