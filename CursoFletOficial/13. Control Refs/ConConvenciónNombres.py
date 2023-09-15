import flet
from flet import Page, Text, TextField, Column, ElevatedButton, Ref

def main(page):
    first_name = Ref[TextField]()
    last_name = Ref[TextField]()
    greetings = Ref[Column]()

    def btn_click(event):
        greetings.current.controls.append(
            Text(f'Hello, {first_name.current.value} {last_name.current.value}')
        )
        first_name.current.value = ""
        last_name.current.value = ""
        page.update()
        first_name.current.focus()

    page.add(
        TextField(ref=first_name, label="First Name", autofocus=True),
        TextField(ref=last_name, label="Last Name"),
        ElevatedButton("Say Hello!", on_click=btn_click),
        Column(ref=greetings)
    )

flet.app(target=main)