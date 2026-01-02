import flet as ft

name = "MenuBar Example"


def example():
    def handle_menu_item_click(e):
        print(f"{e.control.content.value}.on_click")

    return ft.Row(
        [
            ft.MenuBar(
                expand=True,
                style=ft.MenuStyle(
                    alignment=ft.Alignment.TOP_LEFT,
                    bgcolor=ft.Colors.RED_100,
                    mouse_cursor={
                        ft.ControlState.HOVERED: ft.MouseCursor.WAIT,
                        ft.ControlState.DEFAULT: ft.MouseCursor.ZOOM_OUT,
                    },
                ),
                controls=[
                    ft.SubmenuButton(
                        content=ft.Text("File"),
                        controls=[
                            ft.MenuItemButton(
                                content=ft.Text("About"),
                                leading=ft.Icon(ft.Icons.INFO),
                                style=ft.ButtonStyle(
                                    bgcolor={
                                        ft.ControlState.HOVERED: ft.Colors.GREEN_100
                                    }
                                ),
                                on_click=handle_menu_item_click,
                            ),
                            ft.MenuItemButton(
                                content=ft.Text("Save"),
                                leading=ft.Icon(ft.Icons.SAVE),
                                style=ft.ButtonStyle(
                                    bgcolor={
                                        ft.ControlState.HOVERED: ft.Colors.GREEN_100
                                    }
                                ),
                                on_click=handle_menu_item_click,
                            ),
                            ft.MenuItemButton(
                                content=ft.Text("Quit"),
                                leading=ft.Icon(ft.Icons.CLOSE),
                                style=ft.ButtonStyle(
                                    bgcolor={
                                        ft.ControlState.HOVERED: ft.Colors.GREEN_100
                                    }
                                ),
                                on_click=handle_menu_item_click,
                            ),
                        ],
                    ),
                    ft.SubmenuButton(
                        content=ft.Text("View"),
                        controls=[
                            ft.SubmenuButton(
                                content=ft.Text("Zoom"),
                                controls=[
                                    ft.MenuItemButton(
                                        content=ft.Text("Magnify"),
                                        leading=ft.Icon(ft.Icons.ZOOM_IN),
                                        close_on_click=False,
                                        style=ft.ButtonStyle(
                                            bgcolor={
                                                ft.ControlState.HOVERED: ft.Colors.PURPLE_200
                                            }
                                        ),
                                        on_click=handle_menu_item_click,
                                    ),
                                    ft.MenuItemButton(
                                        content=ft.Text("Minify"),
                                        leading=ft.Icon(ft.Icons.ZOOM_OUT),
                                        close_on_click=False,
                                        style=ft.ButtonStyle(
                                            bgcolor={
                                                ft.ControlState.HOVERED: ft.Colors.PURPLE_200
                                            }
                                        ),
                                        on_click=handle_menu_item_click,
                                    ),
                                ],
                            )
                        ],
                    ),
                ],
            )
        ]
    )
