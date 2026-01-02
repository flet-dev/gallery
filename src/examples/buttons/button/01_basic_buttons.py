import flet as ft

name = "Basic Buttons"


def example():
    return ft.Column(
        controls=[
            ft.Button(content="Button"),
            ft.Button("Disabled button", disabled=True),
        ]
    )
