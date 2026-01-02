import flet as ft

name = "SegmentedButton example"


def example():
    color, set_color = ft.use_state(ft.Colors.AMBER)

    bg_container = ft.Container(height=100, expand=True, bgcolor=color)

    def handle_color_click(e):
        set_color(e.control.content.value.lower())

    def handle_on_hover(e):
        print(f"{e.control.content.value}.on_hover")

    menubar = ft.MenuBar(
        expand=True,
        controls=[
            ft.SubmenuButton(
                content=ft.Text("BgColors"),
                controls=[
                    ft.SubmenuButton(
                        content=ft.Text("B"),
                        leading=ft.Icon(ft.Icons.COLORIZE),
                        controls=[
                            ft.MenuItemButton(
                                content=ft.Text("Blue"),
                                style=ft.ButtonStyle(
                                    bgcolor={ft.ControlState.HOVERED: ft.Colors.BLUE}
                                ),
                                on_click=handle_color_click,
                                on_hover=handle_on_hover,
                            )
                        ],
                    ),
                    ft.SubmenuButton(
                        content=ft.Text("G"),
                        leading=ft.Icon(ft.Icons.COLORIZE),
                        controls=[
                            ft.MenuItemButton(
                                content=ft.Text("Green"),
                                style=ft.ButtonStyle(
                                    bgcolor={ft.ControlState.HOVERED: ft.Colors.GREEN}
                                ),
                                on_click=handle_color_click,
                                on_hover=handle_on_hover,
                            )
                        ],
                    ),
                    ft.SubmenuButton(
                        content=ft.Text("R"),
                        leading=ft.Icon(ft.Icons.COLORIZE),
                        controls=[
                            ft.MenuItemButton(
                                content=ft.Text("Red"),
                                style=ft.ButtonStyle(
                                    bgcolor={ft.ControlState.HOVERED: ft.Colors.RED}
                                ),
                                on_click=handle_color_click,
                                on_hover=handle_on_hover,
                            )
                        ],
                    ),
                ],
            )
        ],
    )
    return ft.Column(
        [
            ft.Row([menubar]),
            ft.Row([bg_container]),
        ]
    )
