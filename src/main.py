import logging

import flet as ft

from components.app import App
from models.gallery import Gallery

logging.basicConfig(level=logging.INFO)

gallery = Gallery()
print(gallery)

if __name__ == "__main__":
    ft.run(lambda page: page.render_views(lambda: App(gallery)))
