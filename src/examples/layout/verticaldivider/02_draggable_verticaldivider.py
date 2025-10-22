import flet as ft

name = "Draggable VerticalDivider"


def example():
    width, set_width = ft.use_state(100.0)
    mouse_cursor, set_mouse_cursor = ft.use_state(None)

    def move_vertical_divider(e: ft.DragUpdateEvent):
        if (e.local_delta.x > 0 and width < 300) or (
            e.local_delta.x < 0 and width > 100
        ):
            set_width(width + e.local_delta.x)

    def show_draggable_cursor(e: ft.HoverEvent):
        set_mouse_cursor(ft.MouseCursor.RESIZE_LEFT_RIGHT)

    return ft.Row(
        controls=[
            ft.Container(
                bgcolor=ft.Colors.ORANGE_300,
                alignment=ft.Alignment.CENTER,
                width=width,
            ),
            ft.GestureDetector(
                content=ft.VerticalDivider(),
                mouse_cursor=mouse_cursor,
                drag_interval=10,
                on_pan_update=move_vertical_divider,
                on_hover=show_draggable_cursor,
            ),
            ft.Container(
                bgcolor=ft.Colors.BROWN_400,
                alignment=ft.Alignment.CENTER,
                expand=1,
            ),
        ],
        spacing=0,
        width=400,
        height=400,
    )
