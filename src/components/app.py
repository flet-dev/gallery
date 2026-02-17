import flet as ft

from components.app_bar import AppBar
from components.diagnostics_view import DiagnosticsView
from components.gallery_view import GalleryView
from contexts.route import RouteContext, RouteContextValue
from contexts.theme import ThemeContext, ThemeContextValue
from models.app_model import AppModel
from models.gallery import Gallery


@ft.component
def App(gallery: Gallery) -> ft.View:
    app, _ = ft.use_state(AppModel(route=ft.context.page.route))

    # subscribe to page events as soon as possible
    ft.context.page.on_route_change = app.route_change
    ft.context.page.on_view_pop = app.view_popped

    # stable callbacks (don’t change identity each render)
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

    navigate_callback = ft.use_callback(
        lambda new_route: app.navigate(new_route), dependencies=[app.route]
    )

    route_value = ft.use_memo(
        lambda: RouteContextValue(
            route=app.route,
            navigate=navigate_callback,
        ),
        dependencies=[app.route],
    )

    def on_mounted():
        print("Page size:", ft.context.page.width, ft.context.page.height)
        ft.context.page.title = "Flet controls gallery"
        ft.context.page.fonts = {
            "Roboto Mono": "RobotoMono-VariableFont_wght.ttf",
            "RobotoSlab": "RobotoSlab[wght].ttf",
        }

    ft.on_mounted(on_mounted)

    def update_theme():
        print("Theme mode changed to:", app.theme_mode)
        print("Theme color changed to:", app.theme_color)
        ft.context.page.theme_mode = app.theme_mode
        ft.context.page.theme = ft.context.page.dark_theme = ft.Theme(
            color_scheme_seed=app.theme_color
        )

    ft.on_updated(update_theme, [app.theme_mode, app.theme_color])

    return RouteContext(
        route_value,
        lambda: ThemeContext(
            theme_value,
            lambda: ft.View(
                route="/",
                appbar=AppBar(),
                controls=[
                    DiagnosticsView(key="diagnostics-view")
                    if app.route == "/__diag"
                    else GalleryView(gallery, key="gallery-view")
                ],
            ),
        ),
    )
