import flet as ft

name = "Icons with different colors and sizes"


def example():
    return ft.Row(
        controls=[
            ft.Icon(icon=ft.Icons.FAVORITE, color=ft.Colors.PINK),
            ft.Icon(icon=ft.Icons.AUDIOTRACK, color=ft.Colors.GREEN_400, size=30),
            ft.Icon(icon=ft.Icons.BEACH_ACCESS, color=ft.Colors.BLUE, size=50),
            ft.Icon(icon=ft.Icons.SETTINGS, color=ft.Colors.GREY_400),
        ]
    )
