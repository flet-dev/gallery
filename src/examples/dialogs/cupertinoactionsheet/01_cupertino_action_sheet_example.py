import flet as ft

name = "CupertinoActionSheet Example"


def example():
    action_sheet = ft.CupertinoActionSheet(
        title=ft.Text("Title"),
        message=ft.Text("Message"),
        cancel=ft.CupertinoActionSheetAction(
            content=ft.Text("Cancel"),
            on_click=lambda e: e.control.page.pop_dialog(),
        ),
        actions=[
            ft.CupertinoActionSheetAction(
                content=ft.Text("Default Action"),
                default=True,
                on_click=lambda e: print("Default clicked"),
            ),
            ft.CupertinoActionSheetAction(
                content=ft.Text("Normal Action"),
                on_click=lambda e: print("Normal Action clicked"),
            ),
            ft.CupertinoActionSheetAction(
                content=ft.Text("Destructive Action"),
                destructive=True,
                on_click=lambda e: print("Destructive Action clicked"),
            ),
        ],
    )

    return ft.OutlinedButton(
        "Open CupertinoBottomSheet containing CupertinoActionSheet",
        on_click=lambda e: e.control.page.show_dialog(
            ft.CupertinoBottomSheet(action_sheet)
        ),
    )
