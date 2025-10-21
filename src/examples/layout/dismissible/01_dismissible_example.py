import flet as ft

name = "Dismissible ListView Tiles"


@ft.component
def DismissibleItem(i: int):
    dismissed, set_dismissed = ft.use_state(False)

    return (
        ft.Dismissible(
            content=ft.ListTile(title=ft.Text(f"Item {i}")),
            dismiss_direction=ft.DismissDirection.HORIZONTAL,
            background=ft.Container(bgcolor=ft.Colors.GREEN),
            secondary_background=ft.Container(bgcolor=ft.Colors.RED),
            on_dismiss=lambda e: set_dismissed(True),
            dismiss_thresholds={
                ft.DismissDirection.HORIZONTAL: 0.1,
                ft.DismissDirection.START_TO_END: 0.1,
            },
        )
        if not dismissed
        else None
    )


def example():
    return ft.ListView(
        controls=[c for c in (DismissibleItem(i) for i in range(5)) if c is not None]
    )
