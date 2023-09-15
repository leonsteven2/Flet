#Se renderiza trozos de la pagina poco a poco mediante un método de renderización por partes

import flet
from flet import ListView, Page, Text

def main(page: Page):
    lv_texto = ListView(expand=1, spacing=10, item_extent=50)
    page.add(lv_texto)

    for i in range(5100):
        lv_texto.controls.append(Text(f'Line {i}'))

        if i % 500 == 0:  #Cuando la iteracion i sea multiplo de 500 se actualiza
            page.update()

    page.update()

flet.app(target=main)