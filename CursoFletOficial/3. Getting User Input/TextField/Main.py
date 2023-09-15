import flet
from flet import Page, TextField, Text, IconButton, icons

def main(page: Page):
    def saludar_clicked(event):
        if not txt_nombre.value:
            txt_nombre.error_text = "Por favor ingrese su nombre"
            page.update()
        else:
            nombre = txt_nombre.value
            page.clean()
            page.add(Text("Hola"+nombre))

    txt_nombre = TextField(label="Su nombre")

    page.add(txt_nombre, IconButton(icons.ADD, on_click=saludar_clicked))


flet.app(target=main)