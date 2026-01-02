import flet as ft

name = "FilledButton"


def example():
    return ft.Column(
        controls=[
            ft.FilledButton(content="FilledButton"),
            ft.FilledButton("Disabled button", disabled=True),
            ft.FilledButton("Button with icon", icon=ft.Icons.ADD),
        ]
    )
