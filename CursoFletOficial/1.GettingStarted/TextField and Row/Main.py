import flet
from flet import Page, Row, Text, TextField, ElevatedButton, IconButton, icons

def main(page: Page):
    page.vertical_alignment = "center"

    Letras = ["A","B","C"]
    etiquetas = []

    for i in Letras:
        etiquetas.append(Text(i))

    def saludar(event):
        page.add(Row(controls=[Text("Hola "+str(txt_texto.value)+" ...!")], alignment="center"))
        txt_texto.disabled = False
        page.update()

    txt_texto = TextField(label="Aqui se escribe", disabled=True)

    row_datos = Row(controls=[txt_texto], alignment="center")
    row_datos2 = Row(controls=[Text("1"),Text("2"),Text("3"),ElevatedButton(text="GO", on_click=saludar), IconButton(icons.SMART_BUTTON, visible=False)], alignment="center")

    page.add(row_datos)
    page.add(row_datos2)






flet.app(target=main)

