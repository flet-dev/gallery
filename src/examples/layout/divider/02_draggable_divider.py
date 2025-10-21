import flet as ft

name = "Draggable Divider example"


def example():
    height, set_height = ft.use_state(100.0)
    mouse_cursor, set_mouse_cursor = ft.use_state(None)

    def move_divider(e: ft.DragUpdateEvent):
        if (e.local_delta.y > 0 and height < 300) or (
            e.local_delta.y < 0 and height > 100
        ):
            set_height(height + e.local_delta.y)

    def show_draggable_cursor(e: ft.HoverEvent):
        set_mouse_cursor(ft.MouseCursor.RESIZE_UP_DOWN)

    return ft.Column(
        [
            ft.Container(
                bgcolor=ft.Colors.AMBER,
                alignment=ft.Alignment.CENTER,
                height=height,
            ),
            ft.GestureDetector(
                content=ft.Divider(),
                on_pan_update=move_divider,
                mouse_cursor=mouse_cursor,
                on_hover=show_draggable_cursor,
            ),
            ft.Container(
                bgcolor=ft.Colors.PINK, alignment=ft.Alignment.CENTER, expand=1
            ),
        ],
        spacing=0,
        width=400,
        height=400,
    )
