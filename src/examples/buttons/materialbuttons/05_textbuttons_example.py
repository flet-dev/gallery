import flet as ft

name = "TextButton"


def example():
    return ft.Column(
        [
            ft.TextButton(content="Text button"),
            ft.TextButton("Disabled button", disabled=True),
            ft.TextButton("Button with icon", icon=ft.Icons.ADD),
        ]
    )
