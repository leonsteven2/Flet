import flet
from flet import Page, ElevatedButton, Image

if __name__ == "__main__":
    def main(page: Page):
        page.title = "Pruebas"
        page.add(
            ElevatedButton(
                content=Image(src="C:\\Users\\USER\Downloads\logo.png", width=50, height=50)
            )
        )
    flet.app(target=main)