import flet as ft

from contexts.route import RouteContext
from models.gallery import ControlGroup, ControlItem


@ft.component
def ControlItemView(control_item: ControlItem, group_name: str):
    route_context = ft.use_context(RouteContext)

    def grid_item_clicked(e):
        # use the provided group_name (the currently displayed group)
        # instead of relying on the RouteContext which can be '/' (no group)
        route_context.navigate(f"/{group_name}/{control_item.id}")

    # return ft.Container(
    #     on_click=grid_item_clicked,
    #     bgcolor=ft.Colors.SECONDARY_CONTAINER,
    #     border_radius=5,
    #     padding=15,
    #     content=ft.Row(
    #         alignment=ft.MainAxisAlignment.START,
    #         vertical_alignment=ft.CrossAxisAlignment.CENTER,
    #         controls=[
    #             ft.Icon(ft.Icons.FOLDER_OPEN),
    #             ft.Text(
    #                 value=control_item.name,
    #                 weight=ft.FontWeight.W_500,
    #                 size=14,
    #             ),
    #             # ft.IconButton(icon=ft.Icons.INFO_OUTLINE),
    #         ],
    #     ),
    # )
    return ft.ListTile(
        on_click=grid_item_clicked,
        # bgcolor=ft.Colors.SECONDARY_CONTAINER,
        leading=ft.Icon(ft.Icons.FOLDER_OPEN),
        title=ft.Text(
            value=control_item.name,
            weight=ft.FontWeight.W_500,
            size=14,
        ),
        trailing=ft.IconButton(
            ft.Icons.INFO_OUTLINE,
            tooltip=ft.Tooltip(
                message=control_item.description or "",
                size_constraints=ft.BoxConstraints(max_width=300),
            ),
        ),
    )


@ft.component
def GroupView(group: ControlGroup):
    # return ft.GridView(
    #     expand=True,
    #     runs_count=5,
    #     max_extent=250,
    #     child_aspect_ratio=3.0,
    #     spacing=10,
    #     run_spacing=10,
    #     controls=[
    #         ControlItemView(control_item=control_item)
    #         for control_item in group.controls
    #     ],
    # )
    return ft.ListView(
        expand=True,
        spacing=10,
        padding=10,
        controls=[
            ControlItemView(control_item=control_item, group_name=group.name)
            for control_item in group.controls
        ],
    )
