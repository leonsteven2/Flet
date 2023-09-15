import flet
from flet import Page, ElevatedButton, Container, animation

def main(page: Page):
    contenedor = Container(
        width=150,
        height=150,
        bgcolor="red",
        animate=animation.Animation(1000, "bounceOut")
    )

    def animate_container(event):
        contenedor.width = 100 if contenedor.width == 150 else 150
        contenedor.height = 50 if contenedor.height == 150 else 150
        contenedor.bgcolor = "blue" if contenedor.bgcolor == "red" else "red"
        contenedor.update()

    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    page.spacing = 30

    page.add(
        contenedor,
        ElevatedButton("Animate!", on_click=animate_container)
    )

flet.app(target=main)