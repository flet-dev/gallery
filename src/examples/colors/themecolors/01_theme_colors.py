import flet as ft

name = "Theme colors"


def example():
    class Color:
        def __init__(self, display_name, name, is_dark=False):
            self.name = name
            self.display_name = display_name
            self.is_dark = is_dark

    theme_colors = [
        Color("PRIMARY", "primary"),
        Color("ON_PRIMARY", "onprimary"),
        Color("PRIMARY_CONTAINER", "primarycontainer"),
        Color("ON_PRIMARY_CONTAINER", "onprimarycontainer"),
        Color("PRIMARY_FIXED", "primaryfixed"),
        Color("PRIMARY_FIXED_DIM", "primaryfixeddim"),
        Color("ON_PRIMARY_FIXED", "onprimaryfixed"),
        Color("ON_PRIMARY_FIXED_VARIANT", "onprimaryfixedvariant"),
        Color("SECONDARY", "secondary"),
        Color("ON_SECONDARY", "onsecondary"),
        Color("SECONDARY_CONTAINER", "secondarycontainer"),
        Color("ON_SECONDARY_CONTAINER", "onsecondarycontainer"),
        Color("SECONDARY_FIXED", "secondaryfixed"),
        Color("SECONDARY_FIXED_DIM", "secondaryfixeddim"),
        Color("ON_SECONDARY_FIXED", "onsecondaryfixed"),
        Color("ON_SECONDARY_FIXED_VARIANT", "onsecondaryfixedvariant"),
        Color("TERTIARY", "tertiary"),
        Color("ON_TERTIARY", "ontertiary"),
        Color("TERTIARY_CONTAINER", "tertiarycontainer"),
        Color("ON_TERTIARY_CONTAINER", "ontertiarycontainer"),
        Color("TERTIARY_FIXED", "tertiaryfixed"),
        Color("TERTIARY_FIXED_DIM", "tertiaryfixeddim"),
        Color("ON_TERTIARY_FIXED", "ontertiaryfixed"),
        Color("ON_TERTIARY_FIXED_VARIANT", "ontertiaryfixedvariant"),
        Color("ERROR", "error"),
        Color("ON_ERROR", "onerror"),
        Color("ERROR_CONTAINER", "errorcontainer"),
        Color("ON_ERROR_CONTAINER", "onerrorcontainer"),
        Color("SURFACE", "surface"),
        Color("ON_SURFACE", "onsurface"),
        Color("ON_SURFACE_VARIANT", "onsurfacevariant"),
        Color("SURFACE_TINT", "surfacetint"),
        Color("SURFACE_DIM", "surfacedim"),
        Color("SURFACE_BRIGHT", "surfacebright"),
        Color("SURFACE_CONTAINER", "surfacecontainer"),
        Color("SURFACE_CONTAINER_LOW", "surfacecontainerlow"),
        Color("SURFACE_CONTAINER_LOWEST", "surfacecontainerlowest"),
        Color("SURFACE_CONTAINER_HIGH", "surfacecontainerhigh"),
        Color("SURFACE_CONTAINER_HIGHEST", "surfacecontainerhighest"),
        Color("OUTLINE", "outline"),
        Color("OUTLINE_VARIANT", "outlinevariant"),
        Color("SHADOW", "shadow"),
        Color("SCRIM", "scrim"),
        Color("INVERSE_SURFACE", "inversesurface"),
        Color("ON_INVERSE_SURFACE", "oninversesurface"),
        Color("INVERSE_PRIMARY", "inverseprimary"),
    ]

    async def copy_to_clipboard(e):
        await e.control.page.clipboard.set(f"ft.Colors.{e.control.content.value}")
        e.control.page.show_dialog(
            ft.SnackBar(
                ft.Text(f"Copied to clipboard: ft.Colors.{e.control.content.value}"),
                open=True,
            )
        )

    theme_colors_column = ft.Column(spacing=0)

    theme_colors_column.controls = []

    for color in theme_colors:
        if color.is_dark:
            text_color = ft.Colors.SURFACE_TINT
        else:
            text_color = ft.Colors.ON_SURFACE_VARIANT

        theme_colors_column.controls.append(
            ft.Container(
                height=50,
                bgcolor=color.name,
                content=ft.Text(color.display_name, color=text_color),
                alignment=ft.Alignment.CENTER,
                on_click=copy_to_clipboard,
            )
        )

    return ft.Container(border_radius=10, content=theme_colors_column)
