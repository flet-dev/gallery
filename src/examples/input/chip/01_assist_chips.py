import flet as ft

name = "Assist chips"


def example():
    saved_to_favourites, set_saved_to_favourites = ft.use_state(False)

    async def open_google_maps(e):
        await e.control.page.launch_url("https://maps.google.com")

    return ft.Row(
        [
            ft.Chip(
                label=ft.Text(
                    "Save to favourites"
                    if not saved_to_favourites
                    else "Saved to favourites"
                ),
                leading=ft.Icon(
                    ft.Icons.FAVORITE_BORDER_OUTLINED
                    if not saved_to_favourites
                    else ft.Icons.FAVORITE_OUTLINED
                ),
                disabled=saved_to_favourites,
                on_click=lambda e: set_saved_to_favourites(True),
            ),
            ft.Chip(
                label=ft.Text("9 min walk"),
                leading=ft.Icon(ft.Icons.MAP_SHARP),
                on_click=open_google_maps,
            ),
        ]
    )
