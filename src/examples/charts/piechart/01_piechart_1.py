import flet as ft
import flet_charts as fch

name = "PieChart 1"


def example():
    section_index, set_section_index = ft.use_state(-1)

    normal_border = ft.BorderSide(0, ft.Colors.with_opacity(0, ft.Colors.WHITE))
    hovered_border = ft.BorderSide(6, ft.Colors.WHITE)

    def on_chart_event(e: fch.PieChartEvent):
        set_section_index(e.section_index)
        # for idx, section in enumerate(chart.sections):
        #     section.border_side = (
        #         hovered_border if idx == e.section_index else normal_border
        #     )
        # chart.update()

    chart = fch.PieChart(
        sections=[
            fch.PieChartSection(
                value=25,
                color=ft.Colors.BLUE,
                radius=80,
                border_side=normal_border if ??? else hovered_border,
            ),
            fch.PieChartSection(
                value=25,
                color=ft.Colors.YELLOW,
                radius=65,
                border_side=normal_border,
            ),
            fch.PieChartSection(
                value=25,
                color=ft.Colors.PINK,
                radius=60,
                border_side=normal_border,
            ),
            fch.PieChartSection(
                value=25,
                color=ft.Colors.GREEN,
                radius=70,
                border_side=normal_border,
            ),
        ],
        sections_space=1,
        center_space_radius=0,
        on_event=on_chart_event,
        expand=True,
    )

    return chart
