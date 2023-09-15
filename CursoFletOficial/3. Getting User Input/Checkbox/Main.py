import flet
from flet import Page, Checkbox, Text

def main(page: Page):
    def tarea_checked(event):
        lbl_resultado.value = "La casilla esta en modo: " + str(chk_tarea.value)
        page.update()

    lbl_resultado = Text()
    chk_tarea = Checkbox(label="Aprendido a programar",value=False, on_change=tarea_checked)

    page.add(chk_tarea,lbl_resultado)

flet.app(target=main)
