import flet as ft

name = "ExpansionPanelList example"


def example():
    items, set_items = ft.use_state(
        [(0, ft.Colors.GREEN_500), (1, ft.Colors.BLUE_800), (2, ft.Colors.RED_800)]
    )

    def handle_change(e):
        print(f"change on panel with index {e.data}")

    return ft.ExpansionPanelList(
        expand_icon_color=ft.Colors.AMBER,
        elevation=8,
        divider_color=ft.Colors.AMBER,
        on_change=handle_change,
        controls=[
            ft.ExpansionPanel(
                # has no header and content - placeholders will be used
                bgcolor=ft.Colors.BLUE_400,
                expanded=True,
            )
        ]
        + [
            ft.ExpansionPanel(
                key=i,  # for correct difference calculation
                bgcolor=color,
                content=ft.ListTile(
                    title=ft.Text(f"This is in Panel {i}"),
                    subtitle=ft.Text(f"Press the icon to delete panel {i}"),
                    trailing=ft.IconButton(
                        ft.Icons.DELETE,
                        on_click=lambda e, index=i: set_items(
                            [item for item in items if item[0] != index]
                        ),
                    ),
                ),
            )
            for i, color in items
        ],
    )
