from collections.abc import Callable
from dataclasses import dataclass

import flet as ft


@dataclass(frozen=True)
class ThemeContextValue:
    mode: ft.ThemeMode
    seed_color: ft.Colors
    toggle_mode: Callable[[], None]
    set_seed_color: Callable[[ft.Colors], None] = lambda color: None


ThemeContext = ft.create_context(
    ThemeContextValue(
        mode=ft.ThemeMode.LIGHT,
        seed_color=ft.Colors.BLUE,
        toggle_mode=lambda: None,
        set_seed_color=lambda color: None,
    )
)
