import flet
from flet import Page, Container, ElevatedButton


def animate_end(event):
    print("Termino de animar")

def main(page: Page):
    contenedor = Container(
        width = 200,
        height= 200,
        bgcolor="blue",
        border_radius=10,
        animate_opacity=2000,
        on_animation_end=animate_end
    )


    def animate_opacity(event):
        contenedor.opacity = 0 if contenedor.opacity == 1 else 1
        contenedor.update()



    page.add(
        contenedor,
        ElevatedButton(
            "Animate Opactity",
            on_click=animate_opacity,
        )
    )

flet.app(target=main)