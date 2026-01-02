import flet as ft

name = "Add items to dropdown options"


def example():
    options, set_options = ft.use_state([])
    new_option, set_new_option = ft.use_state("")

    def add_clicked(e):
        set_options(lambda cur: cur + [new_option])
        set_new_option("")

    return ft.Column(
        controls=[
            ft.Dropdown(options=[ft.DropdownOption(option) for option in options]),
            ft.Row(
                controls=[
                    ft.TextField(
                        hint_text="Enter item name",
                        value=new_option,
                        on_change=lambda e: set_new_option(e.control.value),
                    ),
                    ft.Button("Add option", on_click=add_clicked),
                ]
            ),
            ft.Text(value=f"Current options: {', '.join(options)}"),
        ]
    )
