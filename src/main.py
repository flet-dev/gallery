import logging

import flet as ft

from components.app import App
from gallerydata import GalleryData

logging.basicConfig(level=logging.INFO)

gallery = GalleryData()
print(gallery)

if __name__ == "__main__":
    ft.run(lambda page: page.render_views(lambda: App(gallery)))
