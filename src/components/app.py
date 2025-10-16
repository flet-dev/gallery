import asyncio

import flet as ft

from components.app_bar import AppBar
from components.gallery_view import GalleryView
from contexts.theme import ThemeContext, ThemeContextValue
from models.app_model import AppModel
from models.gallery import Gallery


@ft.component
def App(gallery: Gallery) -> list[ft.View]:
    app, _ = ft.use_state(AppModel(route=ft.context.page.route))

    # subscribe to page events as soon as possible
    ft.context.page.on_route_change = app.route_change
    ft.context.page.on_view_pop = app.view_popped

    # stable callback (doesn’t change identity each render)
    toggle_mode = ft.use_callback(
        lambda: app.toggle_theme(), dependencies=[app.theme_mode]
    )
    set_theme_color = ft.use_callback(
        lambda color: app.set_theme_color(color), dependencies=[app.theme_color]
    )

    # memoize the provided value so its identity changes only when mode changes
    theme_value = ft.use_memo(
        lambda: ThemeContextValue(
            mode=app.theme_mode,
            seed_color=app.theme_color,
            toggle_mode=toggle_mode,
            set_seed_color=set_theme_color,
        ),
        dependencies=[app.theme_mode, app.theme_color, toggle_mode, set_theme_color],
    )

    ft.on_mounted(
        lambda: print("Page size:", ft.context.page.width, ft.context.page.height)
    )

    def update_theme():
        print("Theme mode changed to:", app.theme_mode)
        print("Theme color changed to:", app.theme_color)
        ft.context.page.theme_mode = app.theme_mode
        ft.context.page.theme = ft.context.page.dark_theme = ft.Theme(
            color_scheme_seed=app.theme_color
        )

    ft.on_updated(update_theme, [app.theme_mode, app.theme_color])

    return ThemeContext(
        theme_value,
        lambda: [
            ft.View(
                route="/",
                appbar=AppBar(),
                controls=[GalleryView(gallery)],
            ),
            *(
                [
                    ft.View(
                        route="/store",
                        appbar=AppBar(),
                        controls=[
                            ft.Button(
                                "Go Home",
                                on_click=lambda _: asyncio.create_task(
                                    ft.context.page.push_route("/")
                                ),
                            ),
                        ],
                    )
                ]
                if app.route == "/store"
                else []
            ),
        ],
    )
