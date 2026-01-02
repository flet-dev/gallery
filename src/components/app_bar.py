import flet as ft
import flet.version


@ft.component
def AppBar():
    return ft.AppBar(
        title=ft.Row(
            [
                ft.Image(src="logo.svg", width=30),
                ft.Text("Flet Gallery"),
            ]
        ),
        center_title=True,
        # bgcolor=ft.Colors.INVERSE_PRIMARY,
        actions=[
            ft.Container(
                padding=10, content=ft.Text(f"Version: {flet.version.flet_version}")
            ),
        ],
    )
