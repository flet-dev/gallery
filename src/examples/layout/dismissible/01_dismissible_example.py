import flet as ft

name = "Dismissible ListView Tiles"


def example():
    items, set_items = ft.use_state([])

    def handle_dismiss(e):
        # remove the dismissed control from a snapshot copy of the state list
        # to avoid "changed size during iteration" when the underlying
        # collection can be modified by the framework during the dismiss event
        set_items([it for it in items.copy() if it is not e.control])

    set_items(
        [
            ft.Dismissible(
                content=ft.ListTile(title=ft.Text(f"Item {i}")),
                dismiss_direction=ft.DismissDirection.HORIZONTAL,
                background=ft.Container(bgcolor=ft.Colors.GREEN),
                secondary_background=ft.Container(bgcolor=ft.Colors.RED),
                on_dismiss=handle_dismiss,
                on_update=lambda e: print("update"),
                on_resize=lambda e: print("resize"),
                dismiss_thresholds={
                    ft.DismissDirection.HORIZONTAL: 0.1,
                    ft.DismissDirection.START_TO_END: 0.1,
                },
            )
            for i in range(5)
        ]
    )

    return ft.ListView(controls=items)
