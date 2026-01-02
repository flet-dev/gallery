import flet as ft

name = "Simple BottomSheet"


def example():
    bs = ft.BottomSheet(
        ft.Container(
            ft.Column(
                [
                    ft.Text("This is sheet's content!"),
                    ft.Button(
                        "Close bottom sheet", on_click=lambda e: e.page.pop_dialog()
                    ),
                ],
                tight=True,
            ),
            padding=10,
        ),
        open=False,
        on_dismiss=lambda e: print("Dismissed!"),
    )

    return ft.Button("Display bottom sheet", on_click=lambda e: e.page.show_dialog(bs))
