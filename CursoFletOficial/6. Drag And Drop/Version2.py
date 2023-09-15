import flet
from flet import Container, Draggable,border, DragTarget, Page, Row, Text, Alignment, colors, alignment, IconButton, icons

def main(page: Page):
    page.title = 'Ejemplo de Drag&Drop'

    def drag_accept(event):
        source = page.get_control(event.src_id)

        #Actualiza el texto dentro de draggable control
        source.content.content.value = 0

        #Resetea el source group
        source.group=""

        #Actualiza el texto dentro de el drag target control
        event.control.content.content.value = 1
        page.update()

    def drag_will_accept(event):
        event.control.content.border = border.all(
            2, colors.RED if event.data == "true" else colors.BLUE
        )
        event.control.update()

    def drag_leave(event):
        event.control.content.border = None
        event.control.update()


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
                    ),
                    content_when_dragging=Container(
                        width=50,
                        height=50,
                        bgcolor=colors.BLUE_GREY_500,
                        border_radius=5
                    ),
                    content_feedback=IconButton(icons.ALARM)
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
                    on_accept=drag_accept,
                    on_will_accept=drag_will_accept,
                    on_leave=drag_leave

                )

            ]



        )
    )

flet.app(target=main)

