import datetime

import flet as ft

name = "TimePicker example"


def example():
    value, set_value = ft.use_state(datetime.time(12, 0))

    return ft.Column(
        controls=[
            ft.Button(
                "Pick time",
                icon=ft.Icons.CALENDAR_MONTH,
                on_click=lambda e: e.control.page.show_dialog(
                    ft.TimePicker(
                        value=value,
                        confirm_text="Confirm",
                        error_invalid_text="Time out of range",
                        help_text="Pick your time slot",
                        on_change=lambda e: set_value(e.control.value),
                    )
                ),
            ),
            ft.Text(f"Selected time: {value.strftime('%H:%M')}"),
        ]
    )
