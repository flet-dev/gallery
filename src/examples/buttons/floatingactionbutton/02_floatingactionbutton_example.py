import flet as ft

name = "FloatingActionButton Pagelet example"


def example():
    count, set_count = ft.use_state(0)

    def fab_pressed(e):
        set_count(count + 1)
        e.control.page.show_dialog(
            ft.SnackBar(ft.Text("Tile was added successfully!"), open=True)
        )

    p = ft.Pagelet(
        content=ft.Column(
            expand=True,
            scroll=ft.ScrollMode.AUTO,
            controls=[ft.ListTile(title=ft.Text(f"Tile {i}")) for i in range(count)],
        ),
        floating_action_button=ft.FloatingActionButton(
            icon=ft.Icons.ADD,
            bgcolor=ft.Colors.LIME_300,
            data=0,
            on_click=fab_pressed,
        ),
        height=200,
    )

    return p
