import flet as ft

name = "Dropdown with editable input field"


def example():
    return ft.Dropdown(
        label="Color",
        editable=True,
        options=[
            ft.DropdownOption("Red"),
            ft.DropdownOption("Green"),
            ft.DropdownOption("Blue"),
        ],
    )
