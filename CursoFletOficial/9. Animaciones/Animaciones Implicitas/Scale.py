import flet
from flet import transform, Page, Container, ElevatedButton, animation

def main(page: Page):

    contenedor = Container(
        width=200,
        height=200,
        bgcolor="blue",
        border_radius=5,
        scale=transform.Scale(scale=1),
        animate_scale=animation.Animation(1000)
    )

    def animate(e):
        contenedor.scale = 2 if contenedor.scale == 1 else 1
        page.update()

    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    page.spacing = 30
    page.add(
        contenedor,
        ElevatedButton("Animate!", on_click=animate)
    )

flet.app(target=main)
