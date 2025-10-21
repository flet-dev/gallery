import flet as ft

name = "Button (ElevatedButton)"


def example():
    return ft.Column(
        controls=[
            ft.Button(content="Button"),
            ft.Button("Disabled button", disabled=True),
            ft.Button("Button with icon", icon=ft.Icons.ADD),
        ]
    )
