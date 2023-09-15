import flet
from flet import Page, Container, ElevatedButton, transform, animation

def main(page: Page):
    contenedor = Container(
        width=150,
        height=150,
        bgcolor="blue",
        border_radius=10,
        offset=transform.Offset(-2,0),
        animate_offset=animation.Animation(1000, "bounceOut")
    )

    def animate(event):
        contenedor.offset = transform.Offset(0,0)
        contenedor.update()

    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    page.spacing = 30

    page.add(
        contenedor,
        ElevatedButton("Reveal", on_click=animate)
    )

flet.app(target=main)