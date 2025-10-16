from typing import cast

import flet as ft

from components.control_view import ControlView
from components.group_view import GroupView
from components.navigation import Navigation
from contexts.route import RouteContext
from models.gallery import Gallery
from utils.route import Route


@ft.component
def GalleryView(gallery: Gallery):
    route_context = ft.use_context(RouteContext)
    route = Route(route_context.route)
    group_name = route.group if route.group else gallery.control_groups[0].name
    control_id = route.control
    group = gallery.get_control_group(group_name) if group_name else None
    control = (
        gallery.get_control(group_name, control_id)
        if group_name and control_id
        else None
    )

    return ft.Row(
        expand=True,
        controls=cast(
            list[ft.Control],
            [
                Navigation(gallery.control_groups, route.group),
                ft.VerticalDivider(width=1),
                (
                    ControlView(control)
                    if control
                    else GroupView(group)
                    if group
                    else ft.Text("Unknown group")
                ),
            ],
        ),
    )
