import flet as ft

name = "FloatingActionButton example"


def example():
    count, set_count = ft.use_state(0)

    async def fab_pressed(e):
        set_count(count + 1)
        await p.show_dialog(
            ft.SnackBar(ft.Text("Tile was added successfully!"), open=True)
        )

    # def on_mounted():
    #     ft.context.page.floating_action_button = ft.FloatingActionButton(
    #         icon=ft.Icons.ADD,
    #         bgcolor=ft.Colors.LIME_300,
    #         data=0,
    #         on_click=fab_pressed,
    #     )

    # def on_unmounted():
    #     ft.context.page.floating_action_button = None
    #     ft.context.page.pop_dialog()

    # ft.on_mounted(on_mounted)
    # ft.on_unmounted(on_unmounted)
    p = ft.Pagelet(
        content=ft.Column(
            controls=[ft.ListTile(title=ft.Text(f"Tile {i}")) for i in range(count)]
        ),
        floating_action_button=ft.FloatingActionButton(
            icon=ft.Icons.ADD,
            bgcolor=ft.Colors.LIME_300,
            data=0,
            on_click=fab_pressed,
        ),
    )

    return p
