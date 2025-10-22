import flet as ft

name = "Row spacing"


def example():
    value, set_value = ft.use_state(0)

    return ft.Column(
        controls=[
            ft.Text("Spacing between items"),
            ft.Slider(
                min=0,
                max=50,
                divisions=50,
                value=value,
                label="{value}",
                on_change=lambda e: set_value(int(e.control.value)),
            ),
            ft.Row(
                expand=True,
                scroll=ft.ScrollMode.AUTO,
                spacing=value,
                controls=[
                    ft.Container(
                        content=ft.Text(value=str(i)),
                        alignment=ft.Alignment.CENTER,
                        width=50,
                        height=50,
                        bgcolor=ft.Colors.AMBER,
                        border_radius=ft.BorderRadius.all(5),
                    )
                    for i in range(1, 11)
                ],
            ),
        ]
    )
