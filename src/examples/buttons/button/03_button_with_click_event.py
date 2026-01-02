import flet as ft

name = "Button with 'click' event"


def example():
    count, set_count = ft.use_state(0)

    def button_clicked(e):
        set_count(count + 1)

    return ft.Column(
        controls=[
            ft.Button("Button with 'click' event", on_click=button_clicked),
            ft.Text(value=f"Button clicked {count} time(s)"),
        ]
    )
