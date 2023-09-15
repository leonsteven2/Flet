import flet
from flet import CrossAxisAlignment, Row, Column, Page, ElevatedButton, Text, TextField, FloatingActionButton,icons, Checkbox

def main(page: Page):
    page.horizontal_alignment = CrossAxisAlignment.CENTER

    def btn_agregar_tarea_on_click(event):

        col_tareas.controls.append(Checkbox(label=txt_tarea.value))

        txt_tarea.value=""
        page.update()

    txt_tarea = TextField(hint_text="¡Qué necesitas hacer¡", expand=True)
    btn_agregar_tarea = FloatingActionButton(icon=icons.ADD, on_click=btn_agregar_tarea_on_click)
    col_tareas = Column()
    col_vista_principal = Column(
        width = 600,
        controls=[
            Row([
                txt_tarea,
                btn_agregar_tarea
            ]),
            col_tareas

        ]
    )

    page.add(
        col_vista_principal
    )

flet.app(target=main)

