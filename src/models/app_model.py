import asyncio
from dataclasses import dataclass

import flet as ft


@ft.observable
@dataclass
class AppModel:
    route: str
    theme_mode: ft.ThemeMode = ft.ThemeMode.LIGHT
    theme_color: ft.Colors = ft.Colors.BLUE

    def route_change(self, e: ft.RouteChangeEvent):
        print("Route changed from:", self.route, "to:", e.route)
        self.route = e.route

    def navigate(self, new_route: str):
        if new_route != self.route:
            print("Navigating to:", new_route)
            asyncio.create_task(ft.context.page.push_route(new_route))

    async def view_popped(self, e: ft.ViewPopEvent):
        print("View popped")
        views = ft.unwrap_component(ft.context.page.views)
        if len(views) > 1:
            await ft.context.page.push_route(views[-2].route)

    def toggle_theme(self):
        self.theme_mode = (
            ft.ThemeMode.DARK
            if self.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )

    def set_theme_color(self, color: ft.Colors):
        self.theme_color = color
