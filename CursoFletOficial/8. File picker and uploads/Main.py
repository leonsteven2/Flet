import flet
from flet import (
    ElevatedButton,
    FilePicker,
    FilePickerResultEvent,
    Page,
    Row,
    Text,
    icons
)

def main(page: Page):
    def pick_files_result(event: FilePickerResultEvent):
        selected_files.value = (
            ", ".join(map(lambda f: f.name, event.files)) if event.files else "Cancelled!"
        )
        selected_files.update()

    pick_files_dialog = FilePicker(on_result=pick_files_result)
    selected_files = Text()

    #Save File dialog
    def save_file_result(event: FilePickerResultEvent):
        save_file_path.value = event.path if event.path else "Cancelled!"
        save_file_path.update()

    save_file_dialog = FilePicker(on_result=save_file_result)
    save_file_path = Text()

    #Open directory dialog
    def get_directory_result(event: FilePickerResultEvent):
        directory_path.value = event.path if event.path else "Cancelled!"
        directory_path.update()

    get_directory_dialog = FilePicker(on_result=get_directory_result)
    directory_path = Text()

    #hide all dialogs in overlay
    page.overlay.extend([pick_files_dialog, save_file_dialog, get_directory_dialog])

    page.add(
        Row(
            [
                ElevatedButton(
                    "Pick Files",
                    icon = icons.UPLOAD_FILE,
                    on_click=lambda _: pick_files_dialog.pick_files(allow_multiple=True)
                ),
                selected_files
            ]
        ),
        Row(
            [
                ElevatedButton(
                    "Save File",
                    icon = icons.SAVE,
                    on_click=lambda _: save_file_dialog.save_file(),
                    disabled=page.web,
                ),
                save_file_path
            ]
        ),
        Row(
            [
                ElevatedButton(
                    "Open Directory",
                    icon = icons.FOLDER_OPEN,
                    on_click=lambda _: get_directory_dialog.get_directory_path(),
                    disabled=page.web,
                ),
                directory_path
            ]
        )
    )


flet.app(target=main)

