from dataclasses import dataclass, field

import flet as ft
import flet_charts as fch

name = "PieChart 1"

normal_border = ft.BorderSide(0, ft.Colors.with_opacity(0, ft.Colors.WHITE))
hovered_border = ft.BorderSide(6, ft.Colors.WHITE)


@dataclass
@ft.observable
class SectionData:
    value: int
    radius: int
    color: ft.ColorValue
    hovered: bool = False


@dataclass
class ChartData:
    sections: list[SectionData] = field(default_factory=list)


@ft.component
def PieChartSection(section: SectionData) -> fch.PieChartSection:
    return fch.PieChartSection(
        section.value,
        color=section.color,
        radius=section.radius + 10 if section.hovered else section.radius,
        border_side=hovered_border if section.hovered else normal_border,
    )


@ft.component
def example():
    chart_data, _ = ft.use_state(
        ChartData(
            sections=[
                SectionData(value=25, radius=80, color=ft.Colors.BLUE),
                SectionData(value=25, radius=65, color=ft.Colors.YELLOW),
                SectionData(value=25, radius=60, color=ft.Colors.PINK),
                SectionData(value=25, radius=70, color=ft.Colors.GREEN),
            ]
        )
    )

    def on_chart_event(e):
        for idx, section in enumerate(chart_data.sections):
            section.hovered = idx == e.section_index

    chart = fch.PieChart(
        sections=[PieChartSection(section=section) for section in chart_data.sections],
        sections_space=1,
        center_space_radius=0,
        on_event=on_chart_event,
        expand=True,
    )

    return chart
