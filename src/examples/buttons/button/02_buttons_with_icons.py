import flet as ft

name = "ElevatedButtons with icons"


def example():
    return ft.Column(
        controls=[
            ft.Button("Button with icon", icon=ft.Icons.CHAIR_OUTLINED),
            ft.Button(
                "Button with colorful icon",
                icon=ft.Icons.PARK_ROUNDED,
                icon_color="green400",
            ),
        ]
    )
