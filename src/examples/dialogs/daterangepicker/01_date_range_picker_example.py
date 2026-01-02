import datetime

import flet as ft

name = "DatePicker example"


def example():
    start_value, set_start_value = ft.use_state(
        datetime.datetime(year=2000, month=10, day=1)
    )
    end_value, set_end_value = ft.use_state(
        datetime.datetime(year=2000, month=10, day=15)
    )

    return ft.Column(
        controls=[
            ft.Button(
                "Pick date range",
                icon=ft.Icons.CALENDAR_MONTH,
                on_click=lambda e: e.control.page.show_dialog(
                    ft.DateRangePicker(
                        start_value=start_value,
                        end_value=end_value,
                        on_change=lambda e: [
                            set_start_value(e.control.start_value),
                            set_end_value(e.control.end_value),
                        ],
                    )
                ),
            ),
            ft.Text(
                f"Selected date range: {start_value.strftime('%Y-%m-%d')} - {end_value.strftime('%Y-%m-%d')}"
            ),
        ]
    )
