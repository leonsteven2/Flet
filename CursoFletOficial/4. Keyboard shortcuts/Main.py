import flet
from flet import Page, KeyboardEvent, ElevatedButton, Text

def main(page: Page):
    def on_keyboard(event: KeyboardEvent):
        page.add(
            Text(
                f'Key: {event.key}, Shift: {event.shift}, Control: {event.ctrl}, Alt: {event.alt}'
            )
        )
        if str(event.key) == "Arrow Left":
           page.add(Text("Se presiono Izquierda"))

    page.on_keyboard_event = on_keyboard

    page.add(Text("Presiona una tecla"))

flet.app(target=main)


