from dataclasses import dataclass, field

import flet as ft

name = "Free-hand drawing tool"

ItemID = ft.IdCounter()

MAX_SHAPES_PER_CAPTURE = 30


@ft.observable
@dataclass
class Item:
    x1: float
    y1: float
    x2: float
    y2: float
    id: int = field(default_factory=ItemID)


def example():
    import flet.canvas as cv

    items, set_items = ft.use_state([])
    _, set_last_pos = ft.use_state(None)
    canvas = ft.Ref[ft.BaseControl]()

    def pan_start(e: ft.DragStartEvent):
        set_last_pos((e.local_position.x, e.local_position.y))

    async def pan_update(e: ft.DragUpdateEvent):
        def update_last_pos(prev):
            if prev is not None:
                set_items(
                    lambda cur: cur
                    + [
                        Item(
                            prev[0],
                            prev[1],
                            e.local_position.x,
                            e.local_position.y,
                        )
                    ]
                )
            return (e.local_position.x, e.local_position.y)

        set_last_pos(update_last_pos)

    async def on_updated():
        if len(items) > MAX_SHAPES_PER_CAPTURE:
            await canvas.current.capture()
            set_items([])

    ft.on_updated(on_updated)

    async def clear_canvas():
        await canvas.current.clear_capture()
        set_items([])

    cp = cv.Canvas(
        ref=canvas,
        shapes=[
            cv.Line(
                item.x1,
                item.y1,
                item.x2,
                item.y2,
                paint=ft.Paint(stroke_width=3),
                key=item.id,
            )
            for item in items
        ],
        content=ft.GestureDetector(
            on_pan_start=pan_start,
            on_pan_update=pan_update,
            drag_interval=10,
        ),
        expand=False,
    )

    return ft.Column(
        controls=[
            ft.Button("Clear", on_click=clear_canvas),
            ft.Container(
                cp,
                border=ft.Border.all(2, ft.Colors.BLACK54),
                border_radius=5,
                bgcolor=ft.Colors.SURFACE_CONTAINER,
                width=500,
                height=500,
            ),
        ]
    )
