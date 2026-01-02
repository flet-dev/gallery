import flet as ft

name = "PopupMenuButton example"


def example():
    checked, set_checked = ft.use_state(False)

    def check_item_clicked(e):
        set_checked(not checked)

    pb = ft.PopupMenuButton(
        items=[
            ft.PopupMenuItem(content="Item 1"),
            ft.PopupMenuItem(icon=ft.Icons.POWER_INPUT, content="Check power"),
            ft.PopupMenuItem(
                content=ft.Row(
                    [
                        ft.Icon(ft.Icons.HOURGLASS_TOP_OUTLINED),
                        ft.Text("Item with a custom content"),
                    ]
                ),
                on_click=lambda _: print("Button with a custom content clicked!"),
            ),
            ft.PopupMenuItem(),  # divider
            ft.PopupMenuItem(
                content=ft.Text("Checked item"),
                checked=checked,
                on_click=check_item_clicked,
            ),
        ]
    )

    return pb
