import flet as ft

name = "CupertinoRadio example"


def example():
    radio_value, set_radio_value = ft.use_state(None)
    text_value, set_text_value = ft.use_state("")

    return ft.Column(
        [
            ft.Text("Select your favorite color:"),
            ft.RadioGroup(
                value=radio_value,
                on_change=lambda e: set_radio_value(e.control.value),
                content=ft.Column(
                    [
                        ft.CupertinoRadio(
                            value="red",
                            label="Red - Cupertino Radio",
                            active_color=ft.Colors.RED,
                            inactive_color=ft.Colors.RED,
                        ),
                        ft.Radio(
                            value="green",
                            label="Green - Material Radio",
                            fill_color=ft.Colors.GREEN,
                        ),
                        ft.Radio(
                            value="blue",
                            label="Blue - Adaptive Radio",
                            adaptive=True,
                            active_color=ft.Colors.BLUE,
                            tooltip=ft.Tooltip(
                                size_constraints=ft.BoxConstraints(max_width=300),
                                message="Adaptive Radio shows as CupertinoRadio on macOS and iOS and as Radio on other platforms",
                            ),
                        ),
                    ]
                ),
            ),
            ft.Button(
                content="Submit",
                on_click=lambda e: set_text_value(
                    f"Your favorite color is:  {radio_value}"
                ),
            ),
            ft.Text(value=text_value),
        ]
    )
