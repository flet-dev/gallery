import flet as ft

name = "SearchBar example"


def example():
    async def close_anchor(e):
        text = f"Color {e.control.data}"
        print(f"closing view from {text}")
        await anchor.close_view(text)

    async def open_anchor(e):
        await anchor.open_view()

    def handle_change(e):
        print(f"handle_change e.data: {e.data}")

    def handle_submit(e):
        print(f"handle_submit e.data: {e.data}")

    anchor = ft.SearchBar(
        view_elevation=4,
        divider_color=ft.Colors.AMBER,
        bar_hint_text="Search colors...",
        view_hint_text="Choose a color from the suggestions...",
        on_change=handle_change,
        on_submit=handle_submit,
        on_tap=open_anchor,
        controls=[
            ft.ListTile(title=ft.Text(f"Color {i}"), on_click=close_anchor, data=i)
            for i in range(10)
        ],
    )

    return ft.Column(
        controls=[
            ft.Row(
                alignment=ft.MainAxisAlignment.START,
                controls=[
                    ft.OutlinedButton(
                        "Open Search View",
                        on_click=open_anchor,
                    ),
                ],
            ),
            anchor,
        ],
    )
