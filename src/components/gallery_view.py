import flet as ft

from components.group_controls import GroupControls
from components.navigation import Navigation
from models.gallery import Gallery


@ft.component
def GalleryView(gallery: Gallery):
    return ft.Row(
        expand=True,
        controls=[
            Navigation(gallery.control_groups),
            ft.VerticalDivider(width=1),
            GroupControls(),
        ],
    )
