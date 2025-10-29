import flet as ft

name = "Pagelet example"


def example():
    async def open_pagelet_end_drawer(e):
        await pagelet.show_end_drawer()

    pagelet = ft.Pagelet(
        appbar=ft.AppBar(
            title=ft.Text("Pagelet AppBar title"), bgcolor=ft.Colors.AMBER_ACCENT
        ),
        content=ft.Text("Pagelet body"),
        bgcolor=ft.Colors.AMBER_100,
        bottom_appbar=ft.BottomAppBar(
            bgcolor=ft.Colors.BLUE,
            shape=ft.CircularRectangleNotchShape(),
            content=ft.Row(
                controls=[
                    ft.IconButton(icon=ft.Icons.MENU, icon_color=ft.Colors.WHITE),
                    ft.Container(expand=True),
                    ft.IconButton(icon=ft.Icons.SEARCH, icon_color=ft.Colors.WHITE),
                    ft.IconButton(icon=ft.Icons.FAVORITE, icon_color=ft.Colors.WHITE),
                ]
            ),
        ),
        end_drawer=ft.NavigationDrawer(
            controls=[
                ft.NavigationDrawerDestination(
                    icon=ft.Icons.ADD_TO_HOME_SCREEN_SHARP, label="Item 1"
                ),
                ft.NavigationDrawerDestination(
                    icon=ft.Icons.ADD_COMMENT, label="Item 2"
                ),
            ],
        ),
        floating_action_button=ft.FloatingActionButton(
            "Open", on_click=open_pagelet_end_drawer
        ),
        floating_action_button_location=ft.FloatingActionButtonLocation.CENTER_DOCKED,
        # width=400,
        height=400,
    )

    return pagelet
