import flet as ft

name = "Pick multiple files"


def example():
    file_name, set_file_name = ft.use_state("")

    async def pick_files(e):
        file_picker = ft.FilePicker()
        files_list = await file_picker.pick_files(allow_multiple=True)
        print("list =", files_list)
        if files_list:
            set_file_name(", ".join([f.name for f in files_list]))
        else:
            set_file_name("Cancelled!")

    return ft.Row(
        controls=[
            ft.Button(
                "Pick files",
                icon=ft.Icons.UPLOAD_FILE,
                on_click=pick_files,
            ),
            ft.Text(file_name),
        ]
    )
