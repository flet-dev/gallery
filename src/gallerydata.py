import importlib.util
import os
import sys
from dataclasses import dataclass, field
from os.path import isfile
from pathlib import Path

import flet as ft


@dataclass
class GridItem:
    id: str
    name: str | None = None
    examples: list = field(default_factory=list)
    description: str | None = None


@dataclass
class ExampleItem:
    name: str | None = None
    file_name: str | None = None
    order: int | None = None
    example: str | None = None


@dataclass
class ControlGroup:
    name: str
    label: str
    icon: ft.IconData
    selected_icon: ft.IconData
    grid_items: list[GridItem] = field(default_factory=list)


@dataclass
class GalleryData:
    control_groups: list[ControlGroup] = field(
        default_factory=lambda: [
            # ControlGroup(
            #     name="layout",
            #     label="Layout",
            #     icon=ft.Icons.GRID_VIEW,
            #     selected_icon=ft.Icons.GRID_VIEW_SHARP,
            # ),
            # ControlGroup(
            #     name="navigation",
            #     label="Navigation",
            #     icon=ft.Icons.MENU_SHARP,
            #     selected_icon=ft.Icons.MENU_SHARP,
            # ),
            # ControlGroup(
            #     name="displays",
            #     label="Displays",
            #     icon=ft.Icons.INFO_OUTLINED,
            #     selected_icon=ft.Icons.INFO_SHARP,
            # ),
            ControlGroup(
                name="buttons",
                label="Buttons",
                icon=ft.Icons.SMART_BUTTON_SHARP,
                selected_icon=ft.Icons.SMART_BUTTON_SHARP,
            ),
            # ControlGroup(
            #     name="input",
            #     label="Input",
            #     icon=ft.Icons.INPUT_SHARP,
            #     selected_icon=ft.Icons.INPUT_OUTLINED,
            # ),
            # ControlGroup(
            #     name="dialogs",
            #     label="Dialogs",
            #     icon=ft.Icons.MESSAGE_OUTLINED,
            #     selected_icon=ft.Icons.MESSAGE_SHARP,
            # ),
            # ControlGroup(
            #     name="charts",
            #     label="Charts",
            #     icon=ft.Icons.INSERT_CHART_OUTLINED,
            #     selected_icon=ft.Icons.INSERT_CHART_SHARP,
            # ),
            ControlGroup(
                name="animations",
                label="Animations",
                icon=ft.Icons.ANIMATION_SHARP,
                selected_icon=ft.Icons.ANIMATION_SHARP,
            ),
            # ControlGroup(
            #     name="utility",
            #     label="Utility",
            #     icon=ft.Icons.PAN_TOOL_OUTLINED,
            #     selected_icon=ft.Icons.PAN_TOOL_SHARP,
            # ),
            # ControlGroup(
            #     name="colors",
            #     label="Colors",
            #     icon=ft.Icons.FORMAT_PAINT_OUTLINED,
            #     selected_icon=ft.Icons.FORMAT_PAINT_SHARP,
            # ),
            # ControlGroup(
            #     name="contrib",
            #     label="Contrib",
            #     icon=ft.Icons.MY_LIBRARY_ADD_OUTLINED,
            #     selected_icon=ft.Icons.LIBRARY_ADD_SHARP,
            # ),
        ]
    )

    def __post_init__(self):
        self.import_modules()
        # self.selected_control_group = self.control_groups[0]

    def get_control_group(self, control_group_name):
        for control_group in self.control_groups:
            if control_group.name == control_group_name:
                return control_group
        # return self.control_groups[0]

    def get_control(self, control_group_name, control_name):
        control_group = self.get_control_group(control_group_name)
        for grid_item in control_group.grid_items:
            if grid_item.id == control_name:
                return grid_item
        # return self.control_groups[0].grid_items[0]

    def list_control_dirs(self, dir):
        file_path = os.path.join(str(Path(__file__).parent), "examples", dir)
        control_dirs = [
            f
            for f in os.listdir(file_path)
            if not isfile(f)
            and f not in ["index.py", "images", "__pycache__", ".venv", ".git"]
        ]
        return control_dirs

    def list_example_files(self, control_group_dir, control_dir):
        file_path = os.path.join(
            str(Path(__file__).parent), "examples", control_group_dir, control_dir
        )
        example_files = [f for f in os.listdir(file_path) if not f.startswith("_")]
        return example_files

    def import_modules(self):
        for control_group in self.control_groups:
            for control_dir in self.list_control_dirs(control_group.name):
                grid_item = GridItem(control_dir)

                for file in self.list_example_files(control_group.name, control_dir):
                    file_name = os.path.join(control_group.name, control_dir, file)
                    module_name = file_name.replace("/", ".").replace(".py", "")

                    if module_name in sys.modules:
                        print(f"{module_name!r} already in sys.modules")
                    else:
                        file_path = os.path.join(
                            str(Path(__file__).parent), "examples", file_name
                        )

                        spec = importlib.util.spec_from_file_location(
                            module_name, file_path
                        )
                        module = importlib.util.module_from_spec(spec)
                        sys.modules[module_name] = module
                        spec.loader.exec_module(module)
                        print(f"{module_name!r} has been imported")
                        if file == "index.py":
                            grid_item.name = module.name
                            grid_item.description = module.description
                        else:
                            example_item = ExampleItem()
                            example_item.example = module.example

                            example_item.file_name = (
                                module_name.replace(".", "/") + ".py"
                            )
                            example_item.name = module.name
                            example_item.order = file[
                                :2
                            ]  # first 2 characters of example file name (e.g. '01')
                            grid_item.examples.append(example_item)
                grid_item.examples.sort(key=lambda x: x.order)
                control_group.grid_items.append(grid_item)
            try:
                control_group.grid_items.sort(key=lambda x: x.name)
            except:
                print(control_group.name, control_group.grid_items)
