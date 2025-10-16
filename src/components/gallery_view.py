import flet as ft

from components.group_controls import GroupControls
from components.navigation import Navigation
from gallerydata import GalleryData


@ft.component
def GalleryView(gallery: GalleryData):
    return ft.Row(
        expand=True,
        controls=[
            Navigation(gallery.control_groups),
            ft.VerticalDivider(width=1),
            GroupControls(),
        ],
    )
