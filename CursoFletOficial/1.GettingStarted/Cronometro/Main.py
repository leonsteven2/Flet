import time
import flet
from flet import Page, Text

def main(page: Page):
    lbl_texto = Text()
    page.add(lbl_texto)

    for i in range(10):
        lbl_texto.value = "Step: " + str(i)  #f'Step: {i}'
        page.update()

        time.sleep(1)

flet.app(target=main)
