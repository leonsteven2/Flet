from typing import Dict

import flet
from flet import (
    ElevatedButton,
    FilePicker,
    FilePickerResultEvent,
    FilePickerUploadEvent,
    FilePickerUploadFile,
    Page,
    ProgressRing,
    Ref,
    Row,
    Text,
    icons,
    Column
)

def main(page: Page):
    prog_bars: Dict[str, ProgressRing] = {}
    files = Ref[Column]()
    upload_button = Ref[ElevatedButton]()

    def file_picker_result(event: FilePickerResultEvent):
        upload_button.current.disabled = True if event.files == None else False
        prog_bars.clear()
        files.current.controls.clear()
        if event.files != None:
            for f in event.files:
                prog = ProgressRing(value=0, bgcolor="#eeeeee", width=20, height=20)
                prog_bars[f.name] = prog
                files.current.controls.append(Row([prog, Text(f.name)]))
        page.update()


    def on_upload_progress(event: FilePickerUploadEvent):
        prog_bars[event.file_name].value = event.progress
        prog_bars[event.file_name].update()

    file_picker = FilePicker(on_result=file_picker_result, on_upload=on_upload_progress)

    def upload_files(event):
        uf = []
        if file_picker_result is not None and file_picker.result.files is not None:
            for f in file_picker.result.files:
                uf.append(
                    FilePickerUploadFile(
                        f.name,
                        upload_url=page.get_upload_url(f.name, 600)
                    )
                )
            file_picker.upload(uf)

    # hide dialog in overlay
    page.overlay.append(file_picker)

    page.add(
        ElevatedButton(
            "Select Files...",
            icon = icons.FOLDER_OPEN,
            on_click=lambda _: file_picker.pick_files(allow_multiple=True)
        ),
        Column(ref=files),
        ElevatedButton(
            "Upload",
            ref=upload_button,
            icon=icons.UPLOAD,
            on_click=upload_files,
            disabled=True
        )

    )

flet.app(target=main, upload_dir="uploads", view=flet.WEB_BROWSER)


