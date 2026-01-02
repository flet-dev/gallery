import flet as ft

name = "Basic TextFields"


def example():
    tb1_value, set_tb1_value = ft.use_state("")
    tb2_value, set_tb2_value = ft.use_state("First name")
    tb3_value, set_tb3_value = ft.use_state("Last name")
    tb4_value, set_tb4_value = ft.use_state("")
    tb5_value, set_tb5_value = ft.use_state("")

    return ft.Column(
        controls=[
            ft.TextField(
                label="Standard",
                value=tb1_value,
                on_change=lambda e: set_tb1_value(e.control.value),
            ),
            ft.TextField(
                label="Disabled",
                disabled=True,
                value=tb2_value,
                on_change=lambda e: set_tb2_value(e.control.value),
            ),
            ft.TextField(
                label="Read-only",
                read_only=True,
                value=tb3_value,
                on_change=lambda e: set_tb3_value(e.control.value),
            ),
            ft.TextField(
                label="With placeholder",
                hint_text="Please enter text here",
                value=tb4_value,
                on_change=lambda e: set_tb4_value(e.control.value),
            ),
            ft.TextField(
                label="With an icon",
                icon=ft.Icons.EMOJI_EMOTIONS,
                value=tb5_value,
                on_change=lambda e: set_tb5_value(e.control.value),
            ),
            ft.Text(
                value=f"Textboxes values are:  '{tb1_value}', '{tb2_value}', '{tb3_value}', '{tb4_value}', '{tb5_value}'."
            ),
        ]
    )
