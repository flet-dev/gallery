import flet as ft

name = "ElevatedButtons with icons"


def example():
    return ft.Column(
        controls=[
            ft.ElevatedButton("Button with icon", icon=ft.Icons.CHAIR_OUTLINED),
            ft.ElevatedButton(
                "Button with colorful icon",
                icon=ft.Icons.PARK_ROUNDED,
                icon_color="green400",
            ),
        ]
    )
