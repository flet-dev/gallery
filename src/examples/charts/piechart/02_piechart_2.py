from dataclasses import dataclass, field

import flet as ft
import flet_charts as fch

name = "PieChart 2"


normal_radius = 50
hover_radius = 60

normal_title_style = ft.TextStyle(
    size=16, color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD
)
hover_title_style = ft.TextStyle(
    size=22,
    color=ft.Colors.WHITE,
    weight=ft.FontWeight.BOLD,
    shadow=ft.BoxShadow(blur_radius=2, color=ft.Colors.BLACK54),
)


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
        title=f"{section.value}%",
        title_style=hover_title_style if section.hovered else normal_title_style,
        color=section.color,
        radius=section.radius + 10 if section.hovered else section.radius,
    )


@ft.component
def example():
    chart_data, _ = ft.use_state(
        ChartData(
            sections=[
                SectionData(value=40, radius=normal_radius, color=ft.Colors.BLUE),
                SectionData(value=30, radius=normal_radius, color=ft.Colors.YELLOW),
                SectionData(value=15, radius=normal_radius, color=ft.Colors.PURPLE),
                SectionData(value=15, radius=normal_radius, color=ft.Colors.GREEN),
            ]
        )
    )

    def on_chart_event(e):
        for idx, section in enumerate(chart_data.sections):
            section.hovered = idx == e.section_index

    chart = fch.PieChart(
        sections=[PieChartSection(section=section) for section in chart_data.sections],
        sections_space=0,
        center_space_radius=40,
        on_event=on_chart_event,
        expand=True,
    )

    return chart
