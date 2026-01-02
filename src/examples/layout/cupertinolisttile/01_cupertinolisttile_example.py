import flet as ft

name = "CupertinoListTile example"


def example():
    return ft.Column(
        [
            ft.CupertinoListTile(
                additional_info=ft.Text("Wed Jan 24"),
                bgcolor_activated=ft.Colors.AMBER_ACCENT,
                leading=ft.Icon(ft.CupertinoIcons.GAME_CONTROLLER),
                title=ft.Text("CupertinoListTile not notched"),
                subtitle=ft.Text("Subtitle"),
                trailing=ft.Icon(ft.CupertinoIcons.ALARM),
                on_click=lambda e: print("CupertinoListTile clicked!"),
            ),
            ft.CupertinoListTile(
                notched=True,
                additional_info=ft.Text("Thu Jan 25"),
                leading=ft.Icon(ft.CupertinoIcons.GAME_CONTROLLER),
                title=ft.Text("CupertinoListTile notched"),
                subtitle=ft.Text("Subtitle"),
                trailing=ft.Icon(ft.CupertinoIcons.ALARM),
                on_click=lambda e: print("CupertinoListTile clicked!"),
            ),
        ]
    )
