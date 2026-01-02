import flet as ft

name = "Tabs example"


def example():
    return ft.Tabs(
        selected_index=1,
        length=3,
        expand=True,
        content=ft.Column(
            expand=True,
            controls=[
                ft.TabBar(
                    tabs=[
                        ft.Tab(label="Tab 1"),
                        ft.Tab(label="Tab 2", icon=ft.Icons.SETTINGS),
                        ft.Tab(
                            label=ft.CircleAvatar(
                                foreground_image_src="https://avatars.githubusercontent.com/u/7119543?s=88&v=4"
                            ),
                        ),
                    ]
                ),
                ft.TabBarView(
                    # expand=True,
                    height=300,
                    controls=[
                        ft.Container(
                            content=ft.Text("This is Tab 1"),
                            alignment=ft.Alignment.CENTER,
                        ),
                        ft.Container(
                            content=ft.Text("This is Tab 2"),
                            alignment=ft.Alignment.CENTER,
                        ),
                        ft.Container(
                            content=ft.Text("This is Tab 3"),
                            alignment=ft.Alignment.CENTER,
                        ),
                    ],
                ),
            ],
        ),
    )
