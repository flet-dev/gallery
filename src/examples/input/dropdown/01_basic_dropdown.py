import flet as ft

name = "Basic dropdown"


def example():
    dropdown_value, set_dropdownvalue = ft.use_state("")

    return ft.Column(
        controls=[
            ft.Dropdown(
                value=dropdown_value,
                options=[
                    ft.DropdownOption("Red"),
                    ft.DropdownOption("Green"),
                    ft.DropdownOption("Blue"),
                ],
                on_text_change=lambda e: set_dropdownvalue(e.control.value),
            ),
            ft.Text(value=f"Dropdown value is:  {dropdown_value}"),
        ]
    )
