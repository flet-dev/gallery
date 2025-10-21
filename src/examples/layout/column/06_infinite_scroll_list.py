import flet as ft

name = "Infinite scroll list"


def example():
    items, set_items = ft.use_state(lambda: list(range(50)))

    def on_scroll(e: ft.OnScrollEvent):
        if e.pixels >= e.max_scroll_extent - 100:
            set_items(items + list(range(len(items), len(items) + 10)))

    return ft.Container(
        ft.Column(
            spacing=10,
            height=200,
            width=200,
            scroll=ft.ScrollMode.ALWAYS,
            scroll_interval=0,
            on_scroll=on_scroll,
            controls=[ft.Text(f"Text line {item}", key=str(item)) for item in items],
        ),
        border=ft.Border.all(1),
    )
