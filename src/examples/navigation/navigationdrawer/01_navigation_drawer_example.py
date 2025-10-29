import flet as ft

name = "NavigationDrawer example"


def example():
    async def open_end_drawer(e):
        await p.show_end_drawer()

    async def open_drawer(e):
        await p.show_drawer()

    p = ft.Pagelet(
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
        drawer=ft.NavigationDrawer(
            controls=[
                ft.NavigationDrawerDestination(
                    icon=ft.Icons.ADD_TO_HOME_SCREEN_SHARP, label="Item 1"
                ),
                ft.NavigationDrawerDestination(
                    icon=ft.Icons.ADD_COMMENT, label="Item 2"
                ),
            ],
        ),
        content=ft.Column(
            [
                ft.Button("Open end drawer", on_click=open_end_drawer),
                ft.Button("Open drawer", on_click=open_drawer),
            ]
        ),
        height=200,
    )

    return p
