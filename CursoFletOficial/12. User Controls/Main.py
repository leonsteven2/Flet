import flet
from flet import UserControl, Text, Page, Column, TextField, ElevatedButton

class GreeterControl(UserControl):
    def build(self):
        lbl_saludo = Text("Hola Mundo!")

        return lbl_saludo

class GreeterControl2(UserControl):
    def build(self):
        return Column([
            TextField(label="Your name"),
            ElevatedButton("Login")
        ])

def main(page: Page):
    page.title = "User Control"

    page.add(GreeterControl2())

flet.app(target=main)