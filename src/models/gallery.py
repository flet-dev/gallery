import importlib.util
import sys
from collections.abc import Callable
from dataclasses import dataclass, field
from pathlib import Path
from typing import ClassVar

import flet as ft


@dataclass
class ExampleItem:
    name: str = ""
    file_name: str | None = None
    order: int | None = None
    example: Callable | None = None


@dataclass
class ControlItem:
    id: str
    name: str
    examples: list[ExampleItem] = field(default_factory=list)
    description: str | None = None


@dataclass
class ControlGroup:
    name: str
    label: str
    icon: ft.IconData
    selected_icon: ft.IconData
    controls: list[ControlItem] = field(default_factory=list)


@dataclass
class Gallery:
    control_groups: list[ControlGroup] = field(
        default_factory=lambda: [
            ControlGroup(
                name="layout",
                label="Layout",
                icon=ft.Icons.GRID_VIEW,
                selected_icon=ft.Icons.GRID_VIEW_SHARP,
            ),
            ControlGroup(
                name="navigation",
                label="Navigation",
                icon=ft.Icons.MENU_SHARP,
                selected_icon=ft.Icons.MENU_SHARP,
            ),
            ControlGroup(
                name="displays",
                label="Displays",
                icon=ft.Icons.INFO_OUTLINED,
                selected_icon=ft.Icons.INFO_SHARP,
            ),
            ControlGroup(
                name="buttons",
                label="Buttons",
                icon=ft.Icons.SMART_BUTTON_SHARP,
                selected_icon=ft.Icons.SMART_BUTTON_SHARP,
            ),
            ControlGroup(
                name="input",
                label="Input",
                icon=ft.Icons.INPUT_SHARP,
                selected_icon=ft.Icons.INPUT_OUTLINED,
            ),
            ControlGroup(
                name="dialogs",
                label="Dialogs",
                icon=ft.Icons.MESSAGE_OUTLINED,
                selected_icon=ft.Icons.MESSAGE_SHARP,
            ),
            ControlGroup(
                name="charts",
                label="Charts",
                icon=ft.Icons.INSERT_CHART_OUTLINED,
                selected_icon=ft.Icons.INSERT_CHART_SHARP,
            ),
            ControlGroup(
                name="multimedia",
                label="Multimedia",
                icon=ft.Icons.AUDIOTRACK_OUTLINED,
                selected_icon=ft.Icons.AUDIOTRACK_SHARP,
            ),
            ControlGroup(
                name="animations",
                label="Animations",
                icon=ft.Icons.ANIMATION_SHARP,
                selected_icon=ft.Icons.ANIMATION_SHARP,
            ),
            ControlGroup(
                name="utility",
                label="Utility",
                icon=ft.Icons.PAN_TOOL_OUTLINED,
                selected_icon=ft.Icons.PAN_TOOL_SHARP,
            ),
            ControlGroup(
                name="colors",
                label="Colors",
                icon=ft.Icons.FORMAT_PAINT_OUTLINED,
                selected_icon=ft.Icons.FORMAT_PAINT_SHARP,
            ),
        ]
    )
    _IGNORED_ENTRIES: ClassVar[set[str]] = {
        "index.py",
        "images",
        "__pycache__",
        ".venv",
        ".git",
    }
    _INDEX_FILE_NAME: ClassVar[str] = "index.py"

    def __post_init__(self):
        self._examples_root = Path(__file__).resolve().parent.parent / "examples"
        self.import_modules()

    def get_control_group(self, group_name: str) -> ControlGroup | None:
        return next((g for g in self.control_groups if g.name == group_name), None)

    def get_control(self, group_name: str, control_id: str) -> ControlItem | None:
        control_group = self.get_control_group(group_name)
        if not control_group:
            return None
        return next((c for c in control_group.controls if c.id == control_id), None)

    def list_control_dirs(self, group_name: str) -> list[str]:
        base_path = self._examples_root / group_name
        if not base_path.exists():
            return []
        return sorted(
            entry.name
            for entry in base_path.iterdir()
            if entry.is_dir() and entry.name not in self._IGNORED_ENTRIES
        )

    def list_example_files(
        self, control_group_dir: str, control_dir: str
    ) -> list[Path]:
        base_path = self._examples_root / control_group_dir / control_dir
        if not base_path.exists():
            return []
        return sorted(
            path
            for path in base_path.iterdir()
            if path.is_file() and not path.name.startswith("_")
        )

    def import_modules(self) -> None:
        for control_group in self.control_groups:
            control_group.controls.clear()
            for control_dir in self.list_control_dirs(control_group.name):
                grid_item = self._build_grid_item(control_group.name, control_dir)
                control_group.controls.append(grid_item)
            control_group.controls.sort(key=lambda item: (item.name or item.id).lower())

    def _build_grid_item(self, group_name: str, control_dir: str) -> ControlItem:
        grid_item = ControlItem(id=control_dir, name=control_dir)
        for file_path in self.list_example_files(group_name, control_dir):
            module = self._import_module(file_path)
            if file_path.name == self._INDEX_FILE_NAME:
                grid_item.name = getattr(module, "name", grid_item.name)
                grid_item.description = getattr(module, "description", None)
                continue

            example_item = ExampleItem(
                name=getattr(module, "name"),
                file_name=str(file_path.relative_to(self._examples_root).as_posix()),
                order=self._parse_example_order(file_path.name),
                example=getattr(module, "example", None),
            )
            grid_item.examples.append(example_item)
        grid_item.examples.sort(
            key=lambda item: (
                item.order is None,
                item.order if item.order is not None else 0,
                (item.name or "").lower(),
            )
        )
        return grid_item

    def _import_module(self, file_path: Path):
        module_name = ".".join(
            file_path.relative_to(self._examples_root).with_suffix("").parts
        )
        if module_name in sys.modules:
            print(f"{module_name!r} already in sys.modules")
            return sys.modules[module_name]

        spec = importlib.util.spec_from_file_location(module_name, file_path)
        if spec is None or spec.loader is None:
            raise ImportError(f"Cannot load spec for {file_path}")

        module = importlib.util.module_from_spec(spec)
        sys.modules[module_name] = module
        spec.loader.exec_module(module)
        print(f"{module_name!r} has been imported")
        return module

    @staticmethod
    def _parse_example_order(file_name: str) -> int | None:
        prefix = file_name.split("_", 1)[0]
        return int(prefix) if prefix.isdigit() else None
