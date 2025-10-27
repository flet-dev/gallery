import flet as ft

name = "Range slider with divisions and labels"


def example():
    start_value, set_start_value = ft.use_state(10)
    end_value, set_end_value = ft.use_state(30)

    def slider_changed(e):
        set_start_value(e.control.start_value)
        set_end_value(e.control.end_value)

    range_slider = ft.RangeSlider(
        min=0,
        max=50,
        start_value=start_value,
        divisions=10,
        end_value=end_value,
        label="{value}%",
        on_change=slider_changed,
    )

    return ft.Column(
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Container(height=30),
            range_slider,
        ],
    )
