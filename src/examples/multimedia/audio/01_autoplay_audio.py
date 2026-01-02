import flet as ft
import flet_audio as fta

name = "Autoplay Audio"


def example():
    audio = fta.Audio(
        src="https://luan.xyz/files/audio/ambient_c_motion.mp3", autoplay=True
    )

    async def pause_audio(e):
        await audio.pause()

    return ft.Column(
        controls=[
            ft.Text(
                "This is an app with background audio. Note: this example "
                "doesn't work in Safari browser."
            ),
            ft.Button("Stop playing", on_click=pause_audio),
        ]
    )
