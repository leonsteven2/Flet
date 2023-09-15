import flet
from flet import Page, Text, Column, TextField, ElevatedButton, Row

def main(page: Page):
    page.title = "Chat App"

    def on_message(mensaje):
        col_mensajes.controls.append(Text(mensaje))
        page.update()

    page.pubsub.subscribe(on_message)

    def send_click(event):
        page.pubsub.send_all(f"{txt_usuario.value}: {txt_mensaje.value}")
        txt_mensaje.value = ""
        page.update()

    col_mensajes = Column()
    txt_usuario = TextField(hint_text='Escriba su usuario', width=150)
    txt_mensaje = TextField(hint_text='Escriba su mensaje', expand=True)
    btn_enviar = ElevatedButton("Enviar", on_click=send_click)

    page.add(col_mensajes, Row(controls=[txt_usuario, txt_mensaje, btn_enviar]))

flet.app(target=main, view=flet.WEB_BROWSER)
