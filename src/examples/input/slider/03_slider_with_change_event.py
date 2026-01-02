import flet as ft

name = "Slider with `change` event"


def example():
    value, set_value = ft.use_state(50)

    def slider_changed(e):
        set_value(e.control.value)

    return ft.Column(
        controls=[
            ft.Text("Slider with 'on_change' event:"),
            ft.Slider(
                value=value,
                min=0,
                max=100,
                divisions=10,
                label="{value}%",
                on_change=slider_changed,
            ),
            ft.Text(value=f"Current slider value: {value}"),
        ]
    )
