import flet as ft

name = "Column horizontal alignments"


def example():
    def column_with_horiz_alignment(align: ft.CrossAxisAlignment):
        return ft.Column(
            [
                ft.Text(str(align), size=10),
                ft.Container(
                    content=ft.Column(
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
                        alignment=ft.MainAxisAlignment.START,
                        horizontal_alignment=align,
                    ),
                    bgcolor=ft.Colors.AMBER_100,
                    width=100,
                ),
            ]
        )

    return ft.Row(
        expand=True,
        scroll=ft.ScrollMode.AUTO,
        controls=[
            column_with_horiz_alignment(ft.CrossAxisAlignment.START),
            column_with_horiz_alignment(ft.CrossAxisAlignment.CENTER),
            column_with_horiz_alignment(ft.CrossAxisAlignment.END),
        ],
        spacing=30,
        alignment=ft.MainAxisAlignment.START,
    )
