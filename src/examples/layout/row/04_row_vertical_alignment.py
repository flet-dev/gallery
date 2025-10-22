import flet as ft

name = "Row vertical alignments"


def example():
    def row_with_vertical_alignment(align: ft.CrossAxisAlignment):
        return ft.Column(
            width=500,
            controls=[
                ft.Text(str(align), size=16),
                ft.Container(
                    content=ft.Row(
                        [
                            ft.Container(
                                content=ft.Text(value=str(i)),
                                alignment=ft.Alignment.CENTER,
                                width=50,
                                height=50,
                                bgcolor=ft.Colors.AMBER_500,
                            )
                            for i in range(1, 4)
                        ],
                        vertical_alignment=align,
                    ),
                    bgcolor=ft.Colors.AMBER_100,
                    height=150,
                ),
            ],
        )

    return ft.Column(
        [
            row_with_vertical_alignment(ft.CrossAxisAlignment.START),
            row_with_vertical_alignment(ft.CrossAxisAlignment.CENTER),
            row_with_vertical_alignment(ft.CrossAxisAlignment.END),
        ]
    )
