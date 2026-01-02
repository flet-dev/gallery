import flet as ft

name = "Column spacing"


def example():
    value, set_value = ft.use_state(0)

    return ft.Column(
        [
            ft.Text("Spacing between items"),
            ft.Slider(
                min=0,
                max=100,
                divisions=10,
                value=value,
                label="{value}",
                width=500,
                on_change=lambda e: set_value(e.control.value),
            ),
            ft.Column(
                spacing=int(value),
                controls=[
                    ft.Container(
                        content=ft.Text(value=str(i)),
                        alignment=ft.Alignment.CENTER,
                        width=50,
                        height=50,
                        bgcolor=ft.Colors.AMBER,
                        border_radius=ft.BorderRadius.all(5),
                    )
                    for i in range(1, 6)
                ],
            ),
        ]
    )
