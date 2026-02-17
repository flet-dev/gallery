import logging

import flet as ft

from components.app import App
from diagnostics import diagnostics
from models.gallery import Gallery


logging.basicConfig(level=logging.INFO)


gallery = Gallery()

if __name__ == "__main__":
    def main(page: ft.Page):
        diagnostics.enable_for_page(page)
        page.render_views(lambda: App(gallery))

    ft.run(main)
