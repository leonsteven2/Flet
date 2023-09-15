import flet
from flet import Page, Text, ListView

def main(page: Page):
    lv_textos = ListView(expand=True, spacing=10)

    for i in range(5000):
        lv_textos.controls.append(Text(f'Line {i}'))

    page.add(lv_textos)

flet.app(target=main)



