import flet as ft

name = "Column spacing"


def example():
    spacing, set_spacing = ft.use_state(0)
    value, set_value = ft.use_state(0)

    def items(count):
        items = []
        for i in range(1, count + 1):
            items.append(
                ft.Container(
                    content=ft.Text(value=str(i)),
                    alignment=ft.Alignment.CENTER,
                    width=50,
                    height=50,
                    bgcolor=ft.Colors.AMBER,
                    border_radius=ft.BorderRadius.all(5),
                )
            )
        return items

    def spacing_slider_change(e):
        set_spacing(int(e.control.value))
        set_value(e.control.value)

    gap_slider = ft.Slider(
        min=0,
        max=100,
        divisions=10,
        value=0,
        label="{value}",
        width=500,
        on_change=spacing_slider_change,
    )

    col = ft.Column(spacing=spacing, controls=items(5))

    return ft.Column([ft.Column([ft.Text("Spacing between items"), gap_slider]), col])
