import flet as ft

name = "Free-hand drawing tool"


# @ft.observable
# @dataclass
class Item:
    def __init__(self, x1: float, y1: float, x2: float, y2: float):
        self.x1 = float(x1)
        self.y1 = float(y1)
        self.x2 = float(x2)
        self.y2 = float(y2)


def example():
    import flet.canvas as cv

    items, set_items = ft.use_state((list[Item]))
    last_pos, set_last_pos = ft.use_state((None, None))

    def pan_start(e: ft.DragStartEvent):
        # state.x = e.local_x
        # state.y = e.local_y
        set_last_pos((e.local_position.x, e.local_position.y))
        print(f"Pan start at: {e.local_position.x}, {e.local_position.y}")

    def pan_update(e: ft.DragUpdateEvent):
        set_items(
            lambda cur: cur
            + [Item(last_pos[0], last_pos[1], e.local_position.x, e.local_position.y)]
        )
        set_last_pos((e.local_position.x, e.local_position.y))

    cp = cv.Canvas(
        shapes=[
            cv.Fill(
                ft.Paint(
                    gradient=ft.PaintLinearGradient(
                        (0, 0), (600, 600), colors=[ft.Colors.CYAN_50, ft.Colors.GREY]
                    )
                )
            ),
        ]
        + [
            cv.Line(
                item.x1,
                item.y1,
                item.x2,
                item.y2,
                paint=ft.Paint(stroke_width=3),
                # key=item.index,
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

    return ft.Container(
        cp,
        border_radius=5,
        width=500,
        height=500,
    )
