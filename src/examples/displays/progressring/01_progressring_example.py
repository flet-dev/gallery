import asyncio

import flet as ft

name = "ProgressRing Example"


def example():
    mounted, set_mounted = ft.use_state(False)
    working, set_working = ft.use_state(False)
    value, set_value = ft.use_state(0.0)
    text, set_text = ft.use_state("Click the button...")

    ft.on_mounted(lambda: set_mounted(True))
    ft.on_unmounted(lambda: set_mounted(False))

    async def button_clicked():
        set_text("Doing something...")
        set_working(True)
        for i in range(0, 101):
            set_value(i * 0.01)
            await asyncio.sleep(0.1)
            if not mounted:
                break
        set_text("Click the button...")
        set_working(False)

    return ft.Column(
        controls=[
            ft.Text(
                "Circular progress indicator",
                theme_style=ft.TextThemeStyle.HEADLINE_SMALL,
            ),
            ft.Row(
                [
                    ft.ProgressRing(width=16, height=16, stroke_width=2, value=value),
                    ft.Text(value=text),
                ]
            ),
            ft.Text(
                "Indeterminate cicrular progress",
                theme_style=ft.TextThemeStyle.HEADLINE_SMALL,
            ),
            ft.Column(
                [ft.ProgressRing(), ft.Text("I'm going to run for ages...")],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            ft.FilledTonalButton("Start", on_click=button_clicked, disabled=working),
        ]
    )
