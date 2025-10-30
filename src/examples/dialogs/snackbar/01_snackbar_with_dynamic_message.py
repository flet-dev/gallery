import flet as ft

name = "SnackBar with dynamic message"


def example():
    counter, set_counter = ft.use_state(0)

    def on_click(e):
        e.control.page.show_dialog(ft.SnackBar(ft.Text(f"Hello {counter}")))
        set_counter(counter + 1)

    return ft.Button("Open SnackBar", on_click=on_click)
