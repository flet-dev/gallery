import flet as ft

name = "IconButton with `click` event"


def example():
    count, set_count = ft.use_state(0)

    def button_clicked(e):
        set_count(count + 1)

    return ft.Column(
        controls=[
            ft.IconButton(
                icon=ft.Icons.PLAY_CIRCLE_FILL_OUTLINED, on_click=button_clicked, data=0
            ),
            ft.Text(f"Button clicked {count} time(s)"),
        ]
    )
