import flet as ft

name = "DropdownM2"


def example():
    return ft.DropdownM2(
        label="Color",
        options=[
            ft.dropdown.Option("Red"),
            ft.dropdown.Option("Green"),
            ft.dropdown.Option("Blue"),
        ],
    )
