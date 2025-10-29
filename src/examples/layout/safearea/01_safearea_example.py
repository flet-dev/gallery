import flet as ft

name = "SafeArea example"


def example():
    counter, set_counter = ft.use_state(0)

    def fab_pressed(e):
        set_counter(counter + 1)

    p = ft.Pagelet(
        content=ft.SafeArea(
            ft.Container(
                content=ft.Text(str(counter), size=50),
                alignment=ft.Alignment.CENTER,
            )
        ),
        floating_action_button_location=ft.FloatingActionButtonLocation.CENTER_TOP,
        floating_action_button=ft.FloatingActionButton(
            icon=ft.Icons.ADD,
            bgcolor=ft.Colors.LIME_300,
            data=0,
            on_click=fab_pressed,
        ),
        height=400,
    )
    return p
