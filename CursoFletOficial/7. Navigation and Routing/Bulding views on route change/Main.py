import flet
from flet import AppBar, ElevatedButton, Page, Text, View, colors

def main(page: Page):
    page.title = "Ejemplo de Rutas"

    print("Ruta Inicial: ", page.route)

    def route_change(event):
        print("Ruta Cambiada: ", event.route)
        page.views.clear()
        page.views.append(
            View(
                '/',
                [
                    AppBar(title=Text('Flet app')),
                    ElevatedButton("Go to Settings", on_click=open_settings),
                ]
            )
        )

        if page.route == "/settings" or page.route == "/settings/mail":
            page.views.append(
                View(
                    "/settings",
                    [
                        AppBar(title=Text("Settings"), bgcolor=colors.SURFACE_VARIANT),
                        Text("Settings!",style="bodyMedium"),
                        ElevatedButton("Go to mail settings", on_click=open_mail_settings),
                    ]
                )
            )
        if page.route == "/settings/mail":
            page.views.append(
                View(
                    "/settings/mail",
                    [
                        AppBar(
                            title=Text("Mail Settings"), bgcolor=colors.SURFACE_VARIANT
                        ),
                        Text("Mail Settings!")
                    ]
                )
            )
        page.update()

    def view_pop(event):
        print("View pop: ", event.view)
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop

    def open_mail_settings(event):
        page.go("/settings/mail")

    def open_settings(event):
        page.go("/settings")

    page.go(page.route)

flet.app(target=main)


