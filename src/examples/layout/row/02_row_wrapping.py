import flet as ft

name = "Row wrapping"


def example():
    value, set_value = ft.use_state(100)

    return ft.Column(
        controls=[
            ft.Text(
                "Change the row width to see how child items wrap onto multiple rows:"
            ),
            ft.Slider(
                min=0,
                max=500,
                divisions=20,
                value=value,
                label="{value}",
                on_change=lambda e: set_value(float(e.control.value)),
            ),
            ft.Row(
                wrap=True,
                spacing=10,
                run_spacing=10,
                controls=[
                    ft.Container(
                        content=ft.Text(value=str(i)),
                        alignment=ft.Alignment.CENTER,
                        width=50,
                        height=50,
                        bgcolor=ft.Colors.AMBER,
                        border_radius=ft.BorderRadius.all(5),
                    )
                    for i in range(1, 31)
                ],
                width=value,
            ),
        ]
    )
