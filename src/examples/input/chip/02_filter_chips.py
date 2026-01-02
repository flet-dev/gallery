import flet as ft

name = "Filter chips"


def example():
    amenities = ["Washer / Dryer", "Ramp access", "Dogs OK", "Cats OK", "Smoke-free"]

    return ft.Column(
        controls=[
            ft.Row([ft.Icon(ft.Icons.HOTEL_CLASS), ft.Text("Amenities")]),
            ft.Row(
                [
                    ft.Chip(
                        label=ft.Text(amenity),
                        on_select=lambda e: print(
                            f"Selected amenity: {e.control.label.value}"
                        ),
                    )
                    for amenity in amenities
                ]
            ),
        ]
    )
