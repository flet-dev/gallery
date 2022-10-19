import time
from math import pi

import flet
from flet import Column, Icon, Page, Text, icons

from controls.collapsible import Collapsible
from controls.menu_button import MenuButton


def main(page: Page):

    page.scroll = "auto"
    page.add(
        Column(
            [
                Collapsible(
                    "Buttons",
                    icon=Icon(icons.SMART_BUTTON),
                    content=Column(
                        [
                            MenuButton("Basic buttons"),
                            MenuButton("Floating action button"),
                            MenuButton("Popup menu button", selected=True),
                        ],
                        spacing=3,
                    ),
                ),
                Collapsible(
                    "Simple apps",
                    icon=Icon(icons.NEW_RELEASES),
                    content=Column(
                        [
                            MenuButton("Basic buttons"),
                            MenuButton("Floating action button"),
                            MenuButton("Popup menu button", selected=True),
                        ],
                        spacing=3,
                    ),
                ),
                Collapsible(
                    "Forms",
                    icon=Icon(icons.DYNAMIC_FORM),
                    content=Column(
                        [
                            MenuButton("Basic buttons"),
                            MenuButton("Floating action button"),
                            MenuButton("Popup menu button", selected=True),
                        ],
                        spacing=3,
                    ),
                ),
            ],
            spacing=3,
            width=230,
        )
    )


flet.app(port=8550, target=main, view=flet.WEB_BROWSER)
