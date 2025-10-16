import flet as ft

from contexts.theme import ThemeContext
from models.gallery import ControlGroup


@ft.component
def Groups(control_groups: list[ControlGroup]):
    return ft.Column(
        expand=True,
        spacing=0,
        scroll=ft.ScrollMode.ALWAYS,
        width=200,
        controls=[
            ft.Container(
                ink=True,
                padding=10,
                border_radius=5,
                content=ft.Row([ft.Icon(group.icon), ft.Text(group.label)]),
                on_click=lambda e, name=group.name: print(f"Group {name} clicked"),
            )
            for group in control_groups
        ],
    )


@ft.component
def PopupColorItem(color: ft.Colors, name: str) -> ft.PopupMenuItem:
    theme = ft.use_context(ThemeContext)
    return ft.PopupMenuItem(
        content=ft.Row(
            controls=[
                ft.Icon(ft.Icons.COLOR_LENS_OUTLINED, color=color),
                ft.Text(name),
            ],
        ),
        on_click=lambda: theme.set_seed_color(color),
    )


@ft.component
def ThemeModeToggle():
    theme = ft.use_context(ThemeContext)
    return ft.Row(
        [
            ft.IconButton(
                icon=ft.Icons.DARK_MODE
                if theme.mode == ft.ThemeMode.DARK
                else ft.Icons.LIGHT_MODE,
                tooltip="Toggle theme brightness",
                on_click=lambda: theme.toggle_mode(),
            ),
            ft.Text(
                value="Light mode" if theme.mode == ft.ThemeMode.LIGHT else "Dark mode"
            ),
        ]
    )


@ft.component
def ThemeSeedColor():
    theme = ft.use_context(ThemeContext)
    return ft.Row(
        controls=[
            ft.PopupMenuButton(
                icon=ft.Icons.COLOR_LENS_OUTLINED,
                tooltip="Select theme seed color",
                items=[
                    PopupColorItem(color=ft.Colors.DEEP_PURPLE, name="Deep purple"),
                    PopupColorItem(color=ft.Colors.INDIGO, name="Indigo"),
                    PopupColorItem(color=ft.Colors.BLUE, name="Blue (default)"),
                    PopupColorItem(color=ft.Colors.TEAL, name="Teal"),
                    PopupColorItem(color=ft.Colors.GREEN, name="Green"),
                    PopupColorItem(color=ft.Colors.YELLOW, name="Yellow"),
                    PopupColorItem(color=ft.Colors.ORANGE, name="Orange"),
                    PopupColorItem(color=ft.Colors.DEEP_ORANGE, name="Deep orange"),
                    PopupColorItem(color=ft.Colors.PINK, name="Pink"),
                ],
            ),
            ft.Text(theme.seed_color.name.replace("_", " ").title()),
        ]
    )


@ft.component
def ThemeOptions():
    return ft.Column(
        controls=[
            ThemeModeToggle(),
            ThemeSeedColor(),
        ],
    )


@ft.component
def Navigation(control_groups: list[ControlGroup]):
    return ft.Column(
        controls=[
            Groups(control_groups),
            ThemeOptions(),
        ],
    )
