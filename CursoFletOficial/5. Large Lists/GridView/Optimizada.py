import os
import flet
from flet import Container, Page, Row, Text, alignment, border, border_radius, colors, GridView

os.environ['FLET_WS_MAX_MESSAGE_SIZE'] = '8000000'

def main(page: Page):
    gv_datos = GridView(expand=True, max_extent=150, child_aspect_ratio = 0.5)
    page.add(gv_datos)

    for i in range(1000):
        gv_datos.controls.append(
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

flet.app(target=main)