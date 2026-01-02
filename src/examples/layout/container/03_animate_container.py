import flet as ft

name = "Animate container"


def example():
    width, set_width = ft.use_state(200)
    height, set_height = ft.use_state(200)
    bgcolor, set_bgcolor = ft.use_state(ft.Colors.RED)

    def animate_container(e):
        set_width(100 if width == 200 else 200)
        set_height(100 if height == 200 else 200)
        set_bgcolor(ft.Colors.BLUE if bgcolor == ft.Colors.RED else ft.Colors.RED)

    return ft.Column(
        controls=[
            ft.Container(
                width=width,
                height=height,
                bgcolor=bgcolor,
                animate=ft.Animation(1000, ft.AnimationCurve.BOUNCE_OUT),
            ),
            ft.Button("Animate container", on_click=animate_container),
        ]
    )
