import flet as ft

name = "Customize Theme colors"


def example():
    button_text, set_button_text = ft.use_state("Set Primary Color to GREEN")

    def set_primary_color(e):
        e.control.page.theme = ft.Theme(
            color_scheme=ft.ColorScheme(
                primary=ft.Colors.GREEN
                if button_text == "Set Primary Color to GREEN"
                else ft.Colors.BLUE,
            ),
        )
        set_button_text(
            "Set Primary Color to BLUE"
            if button_text == "Set Primary Color to GREEN"
            else "Set Primary Color to GREEN"
        )
        e.control.page.update()

    return ft.Column(
        controls=[ft.FilledButton(button_text, on_click=set_primary_color)]
    )
