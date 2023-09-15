import flet
from flet import Page, Text

def main(page: Page):
    lbl_texto = Text(
        value="Hola Mundo",
        size=30,
        color="green",
        bgcolor="pink",
        weight="bold",
        italic=True
    )

    page.add(lbl_texto)

flet.app(target=main)