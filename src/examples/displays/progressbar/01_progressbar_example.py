import asyncio

import flet as ft

name = "ProgressBar Example"


def example():
    mounted, set_mounted = ft.use_state(False)
    working, set_working = ft.use_state(False)
    value, set_value = ft.use_state(0.0)

    ft.on_mounted(lambda: set_mounted(True))
    ft.on_unmounted(lambda: set_mounted(False))

    async def button_clicked():
        set_working(True)
        set_value(0.0)
        for i in range(0, 101):
            set_value(i * 0.01)
            await asyncio.sleep(0.1)
            if not mounted:
                break
        set_working(False)

    return ft.Column(
        [
            ft.Text(
                "Linear progress indicator",
                theme_style=ft.TextThemeStyle.HEADLINE_SMALL,
            ),
            ft.Column(
                [
                    ft.Text(
                        value="Click the button..."
                        if not working
                        else "Doing something..."
                    ),
                    ft.ProgressBar(value=value, width=400),
                ]
            ),
            ft.Text(
                "Indeterminate progress bar",
                theme_style=ft.TextThemeStyle.HEADLINE_SMALL,
            ),
            ft.ProgressBar(width=400, color="amber", bgcolor="#eeeeee"),
            ft.FilledTonalButton("Start", disabled=working, on_click=button_clicked),
        ]
    )
