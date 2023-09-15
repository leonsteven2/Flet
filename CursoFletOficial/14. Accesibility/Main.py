#Programa para personas no videntes, al presionar CTRL+S se genera una ayuda para estas personas
import flet
from flet import MainAxisAlignment, CrossAxisAlignment, Text, Page, FloatingActionButton, icons, KeyboardEvent

def main(page: Page):
    page.title = "Flet Counter Example"
    page.vertical_alignment = MainAxisAlignment.CENTER
    page.horizontal_alignment = CrossAxisAlignment.CENTER

    def on_keyboard(event: KeyboardEvent):
        print(event)
        if event.key == "S" and event.ctrl:
            page.show_semantics_debugger = not page.show_semantics_debugger
            page.update()

    page.on_keyboard_event = on_keyboard
    txt_number = Text("0", size=40)

    def button_click(event):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()

    page.add(
        txt_number,
        Text("Press CTRL+S to toggle semantics debugger"),
        FloatingActionButton(icon=icons.ADD, tooltip="Increment Number", on_click=button_click),
    )

flet.app(target=main)