import flet as ft

name = "Column wrapping"


def example():
    HEIGHT = 400
    value, set_value = ft.use_state(HEIGHT)

    return ft.Column(
        [
            ft.Text(
                "Change the column height to see how child items wrap onto multiple columns:"
            ),
            ft.Slider(
                min=0,
                max=HEIGHT,
                divisions=20,
                value=value,
                label="{value}",
                width=500,
                on_change=lambda e: set_value(e.control.value),
            ),
            ft.Container(
                content=ft.Column(
                    wrap=True,
                    spacing=10,
                    run_spacing=10,
                    controls=[
                        ft.Container(
                            content=ft.Text(value=str(i)),
                            alignment=ft.Alignment.CENTER,
                            width=30,
                            height=30,
                            bgcolor=ft.Colors.AMBER,
                            border_radius=ft.BorderRadius.all(5),
                        )
                        for i in range(1, 11)
                    ],
                    height=float(value),
                ),
                bgcolor=ft.Colors.AMBER_100,
            ),
        ]
    )
