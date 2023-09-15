import flet
from flet import TextField, Column, Page, Text, ElevatedButton, Row, Ref

def main(page: Page):
    first_name = TextField(label="First Name", autofocus=True)
    last_name = TextField(label="Last Name")
    greetings = Column()

    def btn_click(event):
        greetings.controls.append(Text(f'Hello, {first_name.value} {last_name.value}'))
        first_name.value = ""
        last_name.value = ""
        page.update()
        first_name.focus()

    page.add(
        first_name,
        last_name,
        ElevatedButton("Say Hello!", on_click=btn_click),
        greetings
    )

flet.app(target=main)