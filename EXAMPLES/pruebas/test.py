import flet
from flet import Page, ElevatedButton, IconButton, icons, Row, KeyboardEvent, Text


Contador = 0

def main(page: Page):
    page.title = "Ejemplo de Botones"
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"

    def on_keyboard(event: KeyboardEvent):

        if str(event.key) == "Arrow Left":

           return BotonArriba()

    page.on_keyboard_event = on_keyboard

    def BotonArriba():

        Btn_Arriba.color = "red"

        global Contador
        Contador = Contador + 1

        print(Contador)
        page.update()

    Btn_Arriba = ElevatedButton("A",icon=icons.ARROW_UPWARD)





    page.add(
        Btn_Arriba,
        Row([
            IconButton(icons.ARROW_BACK),
            IconButton(icons.ARROW_DOWNWARD),
            IconButton(icons.ARROW_FORWARD)
        ], alignment="center")
    )

flet.app(target=main)