import os
import flet
from flet import Container, Page, Row, Text, alignment, border, border_radius, colors

os.environ['FLET_WS_MAX_MESSAGE_SIZE'] = '8000000'

def main(page: Page):
    row = Row(wrap=True, scroll="always", expand=True)
    page.add(row)

    for i in range(1000):
        row.controls.append(
            Container(
                Text(f'Item {i}'),
                width=100,
                height=100,
                alignment=alignment.center,
                bgcolor=colors.AMBER_400,
                border=border.all(3, colors.RED),
                border_radius=border_radius.all(100)
            )
        )
    page.update()

flet.app(target=main, view=flet.WEB_BROWSER)