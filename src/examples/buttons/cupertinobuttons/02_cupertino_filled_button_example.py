import flet as ft

name = "CupertinoFilledButton"


def example():
    button = ft.CupertinoFilledButton(
        content=ft.Text("CupertinoFilledButton"),
        opacity_on_click=0.3,
        on_click=lambda e: print("CupertinoFilledButton clicked!"),
    )

    return button
