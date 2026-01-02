import flet as ft

name = "Checkbox with `change` event"


def example():
    checkbox_value, set_checkbox_value = ft.use_state(None)

    return ft.Column(
        controls=[
            ft.Checkbox(
                label="Checkbox with 'change' event",
                value=checkbox_value,
                on_change=lambda e: set_checkbox_value(e.control.value),
            ),
            ft.Text(value=f"Checkbox value changed to {checkbox_value}"),
        ]
    )
