import flet as ft

name = "CupertinoTintedButton"


def example():
    return ft.Column(
        controls=[
            ft.CupertinoTintedButton("CupertinoTintedButton"),
            ft.CupertinoTintedButton("Disabled button", disabled=True),
            ft.CupertinoTintedButton("Button with icon", icon=ft.Icons.ADD),
        ]
    )
