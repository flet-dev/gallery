import flet as ft

from models.gallery import ControlItem, ExampleItem


@ft.component
def Example(example: ExampleItem):
    return ft.Column(
        controls=[
            ft.Container(
                content=ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.Text(
                            example.name,
                            theme_style=ft.TextThemeStyle.TITLE_MEDIUM,
                            weight=ft.FontWeight.W_500,
                            margin=ft.Margin.only(left=5),
                        ),
                        ft.IconButton(
                            icon=ft.Image(
                                src="github-mark.svg",
                                width=24,
                                height=24,
                                color=ft.Colors.ON_SURFACE_VARIANT,
                            ),
                            url=ft.Url(
                                f"https://github.com/flet-dev/gallery/blob/main/src/examples/{example.file_name}",
                                ft.UrlTarget.BLANK,
                            ),
                        ),
                    ],
                ),
                bgcolor=ft.Colors.SECONDARY_CONTAINER,
                padding=5,
                border_radius=5,
            ),
            ft.Container(
                margin=ft.Margin.only(top=20, bottom=20),
                content=example.example(),
                clip_behavior=ft.ClipBehavior.NONE,
            )
            if example.example
            else ft.Text("No example available"),
        ],
    )


@ft.component
def ExampleList(examples: list[ExampleItem]):
    return (
        ft.Column(
            expand=True,
            scroll=ft.ScrollMode.AUTO,
            controls=[Example(example) for example in examples],
        )
        if examples
        else ft.Text("No examples available")
    )


@ft.component
def ControlView(control: ControlItem):
    return ft.Column(
        expand=True,
        controls=[
            ft.Text(value=control.name, theme_style=ft.TextThemeStyle.HEADLINE_MEDIUM),
            *(
                [
                    ft.Text(
                        value=control.description,
                        theme_style=ft.TextThemeStyle.BODY_MEDIUM,
                    )
                ]
                if control.description
                else []
            ),
            ExampleList(control.examples),
        ],
    )
