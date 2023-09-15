import flet
from flet import Page, Text, ElevatedButton

def main(page: Page):
    page.add(Text(f'Ruta Inicial: {page.route}'))

    def route_change(route):
        page.add(Text(f'Nueva Ruta: {route.route}'))

    def go_store(event):
        page.route = "/store"
        page.update()

    page.on_route_change = route_change
    page.add(ElevatedButton("Go to Store", on_click=go_store))

flet.app(target=main, view=flet.WEB_BROWSER)