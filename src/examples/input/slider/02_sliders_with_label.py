import flet as ft

name = "Slider with label"


def example():
    return ft.Column(
        controls=[
            ft.Text("Slider with a custom range and label:"),
            ft.Slider(min=20, max=80, divisions=10, label="{value}%"),
        ]
    )
