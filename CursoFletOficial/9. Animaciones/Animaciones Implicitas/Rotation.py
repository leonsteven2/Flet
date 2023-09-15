from math import pi
import flet
from flet import Page, Container, animation, transform, alignment, ElevatedButton

def main(page: Page):
    contenedor = Container(
        width=100,
        height=70,
        bgcolor="red",
        border_radius=5,
        rotate=transform.Rotate(0, alignment=alignment.center),
        animate_rotation=animation.Animation(duration=5000, curve="bounceOut")
    )

    def animate(event):
        contenedor.rotate.angle += 4*pi
        page.update()

    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    page.spacing = 30
    page.add(
        contenedor,
        ElevatedButton("Animate!", on_click=animate)
    )

flet.app(target=main)

