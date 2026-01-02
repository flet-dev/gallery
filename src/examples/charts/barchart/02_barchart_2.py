from dataclasses import dataclass, field

import flet as ft
import flet_charts as fch

name = "BarChart 2"


@dataclass
@ft.observable
class BarData:
    x: int
    y: float
    axis_label: str
    hovered: bool = False


@dataclass
class ChartData:
    bars: list[BarData] = field(default_factory=list)


@ft.component
def BarChartRod(bar: BarData) -> fch.BarChartRod:
    return fch.BarChartRod(
        to_y=bar.y + 0.5 if bar.hovered else bar.y,
        bg_to_y=20,
        width=22,
        color=ft.Colors.YELLOW if bar.hovered else ft.Colors.WHITE,
        bgcolor=ft.Colors.GREEN_300,
        border_side=(
            ft.BorderSide(width=1, color=ft.Colors.GREEN_400)
            if bar.hovered
            else ft.BorderSide(width=0, color=ft.Colors.WHITE)
        ),
    )


@ft.component
def example():
    chart_data, _ = ft.use_state(
        ChartData(
            bars=[
                BarData(x=0, y=5, axis_label="M"),
                BarData(x=1, y=6.5, axis_label="T"),
                BarData(x=2, y=15, axis_label="W"),
                BarData(x=3, y=7.5, axis_label="T"),
                BarData(x=4, y=9, axis_label="F"),
                BarData(x=5, y=11.5, axis_label="S"),
                BarData(x=6, y=6, axis_label="S"),
            ]
        )
    )

    def on_chart_event(e: fch.BarChartEvent):
        for i, bar in enumerate(chart_data.bars):
            bar.hovered = i == e.group_index

    chart = fch.BarChart(
        groups=[
            fch.BarChartGroup(
                x=bar.x,
                rods=[
                    BarChartRod(bar=bar),
                ],
            )
            for bar in chart_data.bars
        ],
        bottom_axis=fch.ChartAxis(
            labels=[
                fch.ChartAxisLabel(
                    value=bar.x,
                    label=ft.Text(
                        bar.axis_label,
                        color=ft.Colors.BLUE if i % 2 == 0 else ft.Colors.YELLOW,
                    ),
                )
                for i, bar in enumerate(chart_data.bars)
            ],
        ),
        on_event=on_chart_event,
        interactive=True,
    )

    return ft.Container(
        chart,
        bgcolor=ft.Colors.GREEN_200,
        padding=10,
        border_radius=5,
        # expand=True
        width=700,
        height=400,
    )
