import flet as ft

name = "CupertinoPicker example"


def example():
    selected_index, set_selected_index = ft.use_state(3)

    fruits = [
        "Apple",
        "Mango",
        "Banana",
        "Orange",
        "Pineapple",
        "Strawberry",
    ]

    picker = ft.CupertinoPicker(
        selected_index=selected_index,
        # item_extent=40,
        magnification=1.22,
        # diameter_ratio=2,
        squeeze=1.2,
        use_magnifier=True,
        # looping=False,
        on_change=lambda e: set_selected_index(e.control.selected_index),
        controls=[ft.Text(f) for f in fruits],
    )

    return ft.Row(
        tight=True,
        controls=[
            ft.Text("Selected Fruit:", size=23),
            ft.TextButton(
                content=ft.Text(
                    fruits[selected_index],
                    size=23,
                ),
                style=ft.ButtonStyle(color=ft.Colors.BLUE),
                on_click=lambda e: e.control.page.show_dialog(
                    ft.CupertinoBottomSheet(
                        picker,
                        height=216,
                        bgcolor=ft.CupertinoColors.SYSTEM_BACKGROUND,
                        padding=ft.Padding.only(top=6),
                    )
                ),
            ),
        ],
    )
