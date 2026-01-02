import flet as ft
import flet_charts as fch

name = "LineChart 2"


def example():
    toggle, set_toggle = ft.use_state(True)

    data_1 = [
        fch.LineChartData(
            points=[
                fch.LineChartDataPoint(0, 3),
                fch.LineChartDataPoint(2.6, 2),
                fch.LineChartDataPoint(4.9, 5),
                fch.LineChartDataPoint(6.8, 3.1),
                fch.LineChartDataPoint(8, 4),
                fch.LineChartDataPoint(9.5, 3),
                fch.LineChartDataPoint(11, 4),
            ],
            stroke_width=5,
            color=ft.Colors.CYAN,
            curved=True,
            rounded_stroke_cap=True,
        )
    ]

    data_2 = [
        fch.LineChartData(
            points=[
                fch.LineChartDataPoint(0, 3.44),
                fch.LineChartDataPoint(2.6, 3.44),
                fch.LineChartDataPoint(4.9, 3.44),
                fch.LineChartDataPoint(6.8, 3.44),
                fch.LineChartDataPoint(8, 3.44),
                fch.LineChartDataPoint(9.5, 3.44),
                fch.LineChartDataPoint(11, 3.44),
            ],
            stroke_width=5,
            color=ft.Colors.CYAN,
            curved=True,
            rounded_stroke_cap=True,
        )
    ]

    chart = fch.LineChart(
        data_series=data_1 if toggle else data_2,
        border=ft.Border.all(3, ft.Colors.with_opacity(0.2, ft.Colors.PRIMARY)),
        horizontal_grid_lines=fch.ChartGridLines(
            interval=1, color=ft.Colors.with_opacity(0.2, ft.Colors.PRIMARY), width=1
        ),
        vertical_grid_lines=fch.ChartGridLines(
            interval=1, color=ft.Colors.with_opacity(0.2, ft.Colors.PRIMARY), width=1
        ),
        left_axis=fch.ChartAxis(
            labels=[
                fch.ChartAxisLabel(
                    value=1,
                    label=ft.Text("10K", size=14, weight=ft.FontWeight.BOLD),
                ),
                fch.ChartAxisLabel(
                    value=3,
                    label=ft.Text("30K", size=14, weight=ft.FontWeight.BOLD),
                ),
                fch.ChartAxisLabel(
                    value=5,
                    label=ft.Text("50K", size=14, weight=ft.FontWeight.BOLD),
                ),
            ],
            label_size=40,
        ),
        bottom_axis=fch.ChartAxis(
            labels=[
                fch.ChartAxisLabel(
                    value=2,
                    label=ft.Container(
                        ft.Text(
                            "MAR",
                            size=16,
                            weight=ft.FontWeight.BOLD,
                            color=ft.Colors.with_opacity(0.5, ft.Colors.PRIMARY),
                        ),
                        margin=ft.margin.only(top=10),
                    ),
                ),
                fch.ChartAxisLabel(
                    value=5,
                    label=ft.Container(
                        ft.Text(
                            "JUN",
                            size=16,
                            weight=ft.FontWeight.BOLD,
                            color=ft.Colors.with_opacity(0.5, ft.Colors.PRIMARY),
                        ),
                        margin=ft.margin.only(top=10),
                    ),
                ),
                fch.ChartAxisLabel(
                    value=8,
                    label=ft.Container(
                        ft.Text(
                            "SEP",
                            size=16,
                            weight=ft.FontWeight.BOLD,
                            color=ft.Colors.with_opacity(0.5, ft.Colors.PRIMARY),
                        ),
                        margin=ft.margin.only(top=10),
                    ),
                ),
            ],
            label_size=32,
        ),
        tooltip=fch.LineChartTooltip(
            bgcolor=ft.Colors.with_opacity(0.8, ft.Colors.BLUE_GREY)
        ),
        min_y=0,
        max_y=6,
        min_x=0,
        max_x=11,
        # animate=5000,
        # expand=True,
        interactive=True if toggle else False,
        width=700,
        height=500,
    )

    return ft.Column(
        controls=[ft.Button("avg", on_click=lambda e: set_toggle(not toggle)), chart]
    )
