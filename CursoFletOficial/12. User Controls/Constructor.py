import flet
from flet import Page, Text, Row, ElevatedButton, UserControl

class Counter(UserControl):
    def __init__(self, initial_count):
        super().__init__()
        self.counter = initial_count

    def build(self):
        text = Text(str(self.counter))
        def add_click(event):
            self.counter += 1
            text.value = str(self.counter)
            self.update()

        return Row([text, ElevatedButton("Add", on_click=add_click)])

def main(page: Page):
    page.add(
        Counter(100),
        Counter(200)
    )

flet.app(target=main)