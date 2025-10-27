import flet as ft

name = "Basic RadioGroup"


def example():
    radio_value, set_radio_value = ft.use_state("")

    return ft.Column(
        [
            ft.Text("Select your favorite color:"),
            ft.RadioGroup(
                value=radio_value,
                content=ft.Column(
                    [
                        ft.Radio(
                            value="red",
                            label="Red",
                            label_style=ft.TextStyle(color=ft.Colors.RED),
                        ),
                        ft.Radio(
                            value="green",
                            label="Green",
                            label_style=ft.TextStyle(color=ft.Colors.GREEN),
                        ),
                        ft.Radio(
                            value="blue",
                            label="Blue",
                            label_style=ft.TextStyle(color=ft.Colors.BLUE),
                        ),
                    ]
                ),
                on_change=lambda e: set_radio_value(e.control.value),
            ),
            ft.Text(value=f"Your favorite color is:  {radio_value}"),
        ]
    )
