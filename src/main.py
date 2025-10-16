import logging

import flet as ft
import flet.version

from gallerydata import GalleryData

gallery = GalleryData()

logging.basicConfig(level=logging.INFO)

ft.context.disable_auto_update()

print(gallery)


@ft.component
def App():
    count, set_count = ft.use_state(0)

    return ft.Row(
        [
            ft.Text(value=f"{count}"),
            ft.Button("Add", on_click=lambda: set_count(count + 1)),
        ],
    )


ft.run(lambda page: page.render(App))
