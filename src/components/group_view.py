import flet as ft

from contexts.route import RouteContext
from models.gallery import ControlGroup, ControlItem
from utils.route import Route


@ft.component
def ControlItemView(control_item: ControlItem):
    route_context = ft.use_context(RouteContext)

    def grid_item_clicked(e):
        route = Route(route_context.route)
        route_context.navigate(f"/{route.group}/{control_item.id}")

    return ft.Container(
        on_click=grid_item_clicked,
        bgcolor=ft.Colors.SECONDARY_CONTAINER,
        border_radius=5,
        padding=15,
        content=ft.Row(
            alignment=ft.MainAxisAlignment.START,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Icon(ft.Icons.FOLDER_OPEN),
                ft.Text(
                    value=control_item.name,
                    weight=ft.FontWeight.W_500,
                    size=14,
                ),
            ],
        ),
    )


@ft.component
def GroupView(group: ControlGroup):
    return ft.GridView(
        expand=True,
        runs_count=5,
        max_extent=250,
        child_aspect_ratio=3.0,
        spacing=10,
        run_spacing=10,
        controls=[
            ControlItemView(control_item=control_item)
            for control_item in group.controls
        ],
    )
