import flet as ft

name = "Basic checkboxes"


def example():
    c1_value, set_c1_value = ft.use_state(False)
    c2_value, set_c2_value = ft.use_state(None)
    c3_value, set_c3_value = ft.use_state(True)
    c4_value, set_c4_value = ft.use_state(None)
    c5_value, set_c5_value = ft.use_state(None)
    text_value, set_text_value = ft.use_state("")

    return ft.Column(
        controls=[
            ft.Checkbox(
                label="Unchecked by default checkbox",
                value=c1_value,
                on_change=lambda e: set_c1_value(e.control.value),
            ),
            ft.Checkbox(
                label="Undefined by default tristate checkbox",
                tristate=True,
                value=c2_value,
                on_change=lambda e: set_c2_value(e.control.value),
            ),
            ft.Checkbox(
                label="Checked by default checkbox",
                value=c3_value,
                on_change=lambda e: set_c3_value(e.control.value),
            ),
            ft.Checkbox(
                label="Disabled checkbox",
                value=c4_value,
                disabled=True,
                on_change=lambda e: set_c4_value(e.control.value),
            ),
            ft.Checkbox(
                label="Checkbox with rendered label_position='left'",
                value=c5_value,
                label_position=ft.LabelPosition.LEFT,
                on_change=lambda e: set_c5_value(e.control.value),
            ),
            ft.Button(
                content="Submit",
                on_click=lambda e: set_text_value(
                    f"Checkboxes values are:  {c1_value}, {c2_value}, {c3_value}, {c4_value}, {c5_value}."
                ),
            ),
            ft.Text(value=text_value),
        ]
    )
