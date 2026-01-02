import flet as ft

name = "Basic switches"


def example():
    c1_value, set_c1_value = ft.use_state(False)
    c2_value, set_c2_value = ft.use_state(True)
    c3_value, set_c3_value = ft.use_state(False)
    c4_value, set_c4_value = ft.use_state(False)

    return ft.Column(
        controls=[
            ft.Switch(
                label="Unchecked switch",
                value=c1_value,
                on_change=lambda e: set_c1_value(e.control.value),
            ),
            ft.Switch(
                label="Checked switch",
                value=c2_value,
                on_change=lambda e: set_c2_value(e.control.value),
            ),
            ft.Switch(
                label="Disabled switch",
                disabled=True,
                value=c3_value,
                on_change=lambda e: set_c3_value(e.control.value),
            ),
            ft.Switch(
                label="Switch with rendered label_position='left'",
                label_position=ft.LabelPosition.LEFT,
                value=c4_value,
                on_change=lambda e: set_c4_value(e.control.value),
            ),
            ft.Text(
                value=f"Switch values are:  {c1_value}, {c2_value}, {c3_value}, {c4_value}."
            ),
        ]
    )
