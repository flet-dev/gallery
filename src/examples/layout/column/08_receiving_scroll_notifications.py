import flet as ft

name = "Receiving scroll notifications"


def example():
    value, set_value = ft.use_state("No scroll event received yet.")

    return ft.Column(
        [
            ft.Container(
                content=ft.Column(
                    spacing=10,
                    height=200,
                    width=200,
                    scroll=ft.ScrollMode.ALWAYS,
                    controls=[
                        ft.Text(f"Text line {i}", key=str(i)) for i in range(0, 50)
                    ],
                    on_scroll=lambda e: set_value(
                        f"Type: {e.event_type}, pixels: {e.pixels}, min_scroll_extent: {e.min_scroll_extent}, max_scroll_extent: {e.max_scroll_extent}"
                    ),
                ),
                border=ft.Border.all(1),
            ),
            ft.Text(value=value),
        ]
    )
