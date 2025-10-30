import datetime

import flet as ft

name = "DatePicker example"


def example():
    selected_date, set_selected_date = ft.use_state(datetime.datetime.now())

    return ft.Column(
        controls=[
            ft.Button(
                "Pick date",
                icon=ft.Icons.CALENDAR_MONTH,
                on_click=lambda e: e.control.page.show_dialog(
                    ft.DatePicker(
                        first_date=datetime.datetime(2023, 10, 1),
                        last_date=datetime.datetime(2026, 12, 1),
                        value=selected_date,
                        on_change=lambda e: set_selected_date(e.control.value),
                    )
                ),
            ),
            ft.Text(selected_date.strftime("Selected date: %Y-%m-%d")),
        ]
    )
