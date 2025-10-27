import flet as ft

name = "CupertinoSlider example"


def example():
    return ft.Column(
        controls=[
            ft.Text("Cupertino slider:"),
            ft.CupertinoSlider(),
            ft.Text("Material slider:"),
            ft.Slider(),
            ft.Text("Adaptive slider:"),
            ft.Slider(
                adaptive=True,
                tooltip=ft.Tooltip(
                    size_constraints=ft.BoxConstraints(max_width=300),
                    message="Adaptive Slider shows as CupertinoSlider on macOS and iOS and as Slider on other platforms",
                ),
            ),
        ],
    )
