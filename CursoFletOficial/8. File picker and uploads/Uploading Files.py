import flet
from flet import FilePicker, FilePickerResultEvent, FilePickerUploadFile, ElevatedButton

def upload_files(event):
    upload_list = []
    if file_picker.result != None and file_picker.result.files != None:
        for f in file_picker.result.files:
            upload_list.append(
                FilePickerUploadFile(
                    f.name,
                    upload_url=page.get_upload_url(f.name, 600),
                )
            )
            file_picker.upload(upload_list)

ElevatedButton("Upload", on_click=upload_files)