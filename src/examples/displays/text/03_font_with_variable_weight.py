import flet as ft

name = "Font with variable weight"


def example():
    weight, set_weight = ft.use_state(ft.FontWeight.W_100)
    value, set_value = ft.use_state(100)

    def width_changed(e):
        set_weight(f"w{int(e.control.value)}")
        set_value(int(e.control.value))

    return ft.Column(
        controls=[
            ft.Text(
                "This is rendered with Roboto Slab",
                size=30,
                font_family="RobotoSlab",
                weight=weight,
            ),
            ft.Slider(
                value=value,
                min=100,
                max=900,
                divisions=8,
                label="{value}",
                width=500,
                on_change=width_changed,
            ),
        ]
    )
