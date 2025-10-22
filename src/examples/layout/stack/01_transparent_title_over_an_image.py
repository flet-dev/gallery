import flet as ft

name = "Transparent title over an image"


def example():
    return ft.Stack(
        controls=[
            ft.Image(
                src="https://picsum.photos/300/300",
                width=300,
                height=300,
                fit=ft.BoxFit.CONTAIN,
            ),
            ft.Row(
                controls=[
                    ft.Text(
                        value="Image title",
                        color=ft.Colors.WHITE,
                        size=40,
                        weight=ft.FontWeight.BOLD,
                        opacity=0.5,
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
        ],
        width=300,
        height=300,
    )
