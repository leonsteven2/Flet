import flet
from flet import IconButton, Page, Row, TextField, icons, Checkbox, ElevatedButton

def main(page: Page):
    def agregar_tarea_clicked(event):
        page.add(Row(controls=[Checkbox(label=txt_nueva_tarea.value)],alignment="center"))

    txt_nueva_tarea = TextField(hint_text="Escriba su tarea aquí", width=500)
    btn_agregar_tarea = IconButton(icons.ADD, on_click=agregar_tarea_clicked)

    page.add(Row([txt_nueva_tarea,btn_agregar_tarea], alignment="center"))

flet.app(target=main)