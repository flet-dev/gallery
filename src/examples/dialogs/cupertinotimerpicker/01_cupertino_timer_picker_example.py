import time

import flet as ft

name = "CupertinoTimerPicker example"


def example():
    value, set_value = ft.use_state(3600)

    return ft.Row(
        tight=True,
        controls=[
            ft.Text("TimerPicker Value:", size=23),
            ft.TextButton(
                content=ft.Text(
                    time.strftime("%H:%M:%S", time.gmtime(value)),
                    size=23,
                ),
                style=ft.ButtonStyle(color=ft.Colors.RED),
                on_click=lambda e: e.control.page.show_dialog(
                    ft.CupertinoBottomSheet(
                        content=ft.CupertinoTimerPicker(
                            value=value,
                            second_interval=10,
                            minute_interval=1,
                            mode=ft.CupertinoTimerPickerMode.HOUR_MINUTE_SECONDS,
                            on_change=lambda e: set_value(int(e.control.value)),
                        ),
                        height=216,
                        bgcolor=ft.CupertinoColors.SYSTEM_BACKGROUND,
                        padding=ft.Padding.only(top=6),
                    )
                ),
            ),
        ],
    )
