import json

import flet as ft

from diagnostics import diagnostics


@ft.component
def DiagnosticsView() -> ft.Control:
    last_dump, set_last_dump = ft.use_state("No diagnostics dump requested yet.")

    print("Rendering DiagnosticsView")

    def dump_now(_):
        payload = diagnostics.dump_now(reason="hidden_route_button")
        set_last_dump(json.dumps(payload, indent=2, default=str))

    return ft.Column(
        expand=True,
        controls=[
            ft.Text("Memory Diagnostics"),
            ft.Text(
                "Hidden route for on-demand mem diagnostics. Triggering a dump logs JSON via memdiag logger.",
                color=ft.Colors.ON_SURFACE_VARIANT,
            ),
            ft.Row(
                controls=[
                    ft.Button(
                        "Dump diagnostics now",
                        icon=ft.Icons.BUG_REPORT,
                        on_click=dump_now,
                    ),
                    ft.OutlinedButton(
                        "Back to gallery",
                        icon=ft.Icons.ARROW_BACK,
                        on_click=lambda _: ft.context.page.go("/"),
                    ),
                ]
            ),
            ft.TextField(
                value=last_dump,
                multiline=True,
                min_lines=14,
                max_lines=24,
                read_only=True,
                expand=True,
                text_style=ft.TextStyle(font_family="Roboto Mono", size=12),
            ),
        ],
    )
