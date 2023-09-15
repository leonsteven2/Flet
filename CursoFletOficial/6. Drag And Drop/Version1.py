import flet
from flet import Container, Draggable, DragTarget, Page, Row, Text, Alignment, colors, alignment

def main(page: Page):
    page.title = 'Ejemplo de Drag&Drop'

    def drag_accept(event):
        source = page.get_control(event.src_id)

        #Actualiza el texto dentro de draggable control
        source.content.content.value = 0

        #Actualiza el texto dentro de el drag target control
        event.control.content.content.value = 1
        page.update()

    page.add(
        Row(
            [
                Draggable(
                    group="Number",
                    content=Container(
                        width=50,
                        height=50,
                        bgcolor=colors.CYAN_200,
                        border_radius=5,
                        content=Text("1", size=20),
                        alignment=alignment.center
                    )
                ),

                Container(width=100),

                DragTarget(
                    group="Number",
                    content=Container(
                        width=50,
                        height=50,
                        bgcolor=colors.PINK_200,
                        border_radius=5,
                        content=Text("0", size=20),
                        alignment=alignment.center
                    ),
                    on_accept=drag_accept
                )

            ]



        )
    )

flet.app(target=main)

