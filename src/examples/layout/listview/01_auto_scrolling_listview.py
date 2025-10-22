import asyncio

import flet as ft

name = "Auto-scrolling ListView"


def example():
    items, set_items = ft.use_state(list(range(60)))

    async def auto_scroll(e):
        # count = 1
        cur = items.copy()
        for i in range(61, 120):
            await asyncio.sleep(1)

            # lv.controls.append(ft.Text(f"Line {count}"))
            # set_items(items + [i])
            set_items(cur + [i])
            cur = items.copy()
            print(f"Cur: {cur}")

            print(f"Items: {items}")
            # count += 1
            print(f"Scrolling to line {i}")
            # lv.update()

    return ft.Column(
        controls=[
            ft.ListView(
                spacing=10,
                padding=20,
                auto_scroll=True,
                height=300,
                controls=[
                    ft.Text(
                        key=i,
                        value=f"Line {i + 1}",
                    )
                    for i in items
                ],
            ),
            ft.OutlinedButton("Start auto-scrolling", on_click=auto_scroll),
        ]
    )
