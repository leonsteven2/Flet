import flet
from flet import UserControl, Text, Page, Column, TextField, ElevatedButton, Row

class Counter(UserControl):
    def add_click(self, event):
        self.counter += 1
        self.text.value = str(self.counter)
        self.update()

    def build(self):
        self.counter = 0
        self.text = Text(str(self.counter))
        return Row([self.text, ElevatedButton("Add", on_click=self.add_click)])

def main(page: Page):
    page.title = "Contadores"
    page.add(Counter(), Counter())

flet.app(target=main)