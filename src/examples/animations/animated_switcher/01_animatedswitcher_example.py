import flet as ft

name = "Animated switching between two containers with scale effect"


def example():
    alternate, set_alternate = ft.use_state(True)
    print(f"!!!!! alternate: {alternate}")
    return ft.Column(
        controls=[
            ft.AnimatedSwitcher(
                ft.Container(
                    ft.Text("Hello!", theme_style=ft.TextThemeStyle.HEADLINE_MEDIUM),
                    alignment=ft.Alignment.CENTER,
                    width=200,
                    height=200,
                    bgcolor=ft.Colors.GREEN,
                )
                if alternate
                else ft.Container(
                    ft.Text("Bye!", size=50),
                    alignment=ft.Alignment.CENTER,
                    width=200,
                    height=200,
                    bgcolor=ft.Colors.YELLOW,
                ),
                transition=ft.AnimatedSwitcherTransition.SCALE,
                duration=500,
                reverse_duration=100,
                switch_in_curve=ft.AnimationCurve.BOUNCE_OUT,
                switch_out_curve=ft.AnimationCurve.BOUNCE_IN,
            ),
            ft.Button("Animate!", on_click=lambda: set_alternate(not alternate)),
        ]
    )
