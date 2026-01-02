import flet as ft

name = "FAB added as Regular Button"


def example():
    return ft.Column(
        controls=[
            ft.FloatingActionButton(content="Button", icon=ft.Icons.ADD),
            ft.FloatingActionButton(icon=ft.Icons.ADD, disabled=True),
            ft.FloatingActionButton("Mini", mini=True),
        ]
    )
