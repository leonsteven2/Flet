import flet
from flet import Container, animation, transform, Stack, Page, ElevatedButton

def main(page: Page):
    contenedor1 = Container(width=50, height=50, top=0, left=0, bgcolor="red", animate_position=1000)
    contenedor2 = Container(width=50, height=50, top=60, left=0, bgcolor="green", animate_position=2000)
    contenedor3 = Container(width=50, height=50, top=120, left=0, bgcolor="blue", animate_position=3000)

    def animate_container(event):
        contenedor1.top = 20 if contenedor1.top == 0 else 0
        contenedor1.left = 200 if contenedor1.top == 0 else 0

        contenedor2.top = 100 if contenedor1.top == 60 else 60
        contenedor2.left = 40 if contenedor1.top == 0 else 0

        contenedor3.top = 180 if contenedor1.top == 120 else 120
        contenedor3.left = 100 if contenedor1.top == 0 else 0

        page.update()

    page.add(
        Stack([contenedor1,contenedor2,contenedor3],height=250),
        ElevatedButton("Animate!", on_click=animate_container)
    )

flet.app(target=main)

