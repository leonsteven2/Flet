import flet
from flet import Page, TextStyle, FontWeight, TextDecorationStyle, TextAlign, colors, TextCapitalization, Theme, \
    UserControl, Container, margin, icons, ElevatedButton, Image, SafeArea, Checkbox
from flet_core import Text, Column, TextField, Row, ImageFit, TextButton

def ejemplo():
    row_1 = Row(
        controls=[
            Text("Hola")
        ]
    )
    return row_1

class LoginInterface(UserControl):
    def __init__(self):
        super().__init__()
        self.hola = True

    def build(self):
        self.row_interfaz = Row(
            controls=[
                Container(
                    expand=2,
                    alignment=flet.alignment.center,
                    image_src=f'https://i.pinimg.com/originals/67/bb/2f/67bb2f4b121a72681c4f53268416b58b.gif',
                    image_fit=ImageFit.COVER
                ),
                Container(
                    gradient=flet.LinearGradient(
                        begin=flet.alignment.top_center,
                        end=flet.alignment.bottom_center,
                        colors=[colors.PINK_900, colors.BLACK]
                    ),
                    expand=1,
                    content=Container_Login_Password(),
                    alignment=flet.alignment.top_center
                )
            ],
            spacing=3,
        )
        return self.row_interfaz


class CajaTextoConIcono(UserControl):
    def __init__(self, label, src_image, password, icon):
        super().__init__()
        self.label = label
        self.src_image = src_image
        self.password = password
        self.icon = icon

    def build(self):
        row_usuario = Row(
            # alignment=flet.MainAxisAlignment.END,
            controls=[
                # Image(
                #     src=self.src_image,
                #     width=30,
                #     height=30,
                #     fit=flet.ImageFit.CONTAIN,
                # ),
                TextField(
                    # value="ADMIN",
                    icon=self.icon,
                    label=self.label,
                    height=50,
                    expand=1,
                    label_style=TextStyle(
                        color=colors.WHITE,
                        weight=FontWeight.BOLD,
                    ),
                    text_align=TextAlign.JUSTIFY,
                    text_style=TextStyle(
                        color=colors.AMBER,
                        weight=FontWeight.BOLD,
                    ),
                    # border="underline",
                    # border_width=2,
                    border_radius=15,
                    capitalization=TextCapitalization.CHARACTERS,
                    password=self.password,
                    can_reveal_password=self.password,
                    border_color=colors.WHITE,
                    on_focus=True,
                    bgcolor=colors.PINK_ACCENT_700,
                    autofocus=True
                ),

            ]
        )
        return row_usuario


class Container_Login_Password(UserControl):
    def build(self):
        self.container = Container(
            width=350,
            padding=20,
            blur=2,
            content=Column(
                alignment=flet.MainAxisAlignment.CENTER,
                spacing=20,
                controls=[
                    Text("Welcome Back", size=30, color=colors.WHITE),
                    Text(""),
                    CajaTextoConIcono(
                        label="Username",
                        src_image=f'https://cdn-icons-png.flaticon.com/128/6172/6172285.png',
                        password=False,
                        icon=icons.PERSON
                    ),
                    CajaTextoConIcono(
                        label="Password",
                        src_image=f'https://cdn-icons-png.flaticon.com/128/9397/9397489.png',
                        password=True,
                        icon=icons.SECURITY
                    ),
                    Row(
                        # alignment=flet.MainAxisAlignment.CENTER,
                        spacing=30,
                        controls=[
                            Checkbox(label="Remember Password", expand=1),
                            TextButton(text="Forgot Password", expand=1)
                        ]
                    ),
                    Text(""),
                    Row(
                        controls=[
                            ElevatedButton(
                                content=Text(value="Login", size=20),
                                expand=1,
                                color=colors.RED_ACCENT_700,
                                bgcolor=colors.WHITE,
                                style=flet.ButtonStyle(
                                    overlay_color=colors.ON_PRIMARY_CONTAINER,
                                    shape=flet.RoundedRectangleBorder(radius=10),
                                ),
                                on_click=self.start_session,
                            )
                        ],
                    ),
                    Row(
                        alignment=flet.MainAxisAlignment.CENTER,
                        controls=[
                            Text("Dont you have account?", expand=1),
                            TextButton(text="Create account here", expand=1)
                        ]
                    ),


                ],

            ),
            alignment=flet.alignment.top_center,

        )
        return self.container

    def start_session(self, event):
        print("Entrando a la sesión")

        self.update()


if __name__ == "__main__":
    def main(page: Page):
        # page.theme_mode = flet.ThemeMode.LIGHT
        page.title = "Login Interface"
        page.fonts = {
            "Kanit": "https://raw.githubusercontent.com/google/fonts/master/ofl/kanit/Kanit-Bold.ttf",
            "Oswald Bold": "https://github.com/googlefonts/OswaldFont/raw/main/fonts/ttf/Oswald-Bold.ttf",
        }
        page.theme = Theme(font_family="Oswald Bold")

        login_interface = LoginInterface()

        page.add(
            # Agregamos la interfaz de inicio del usuario
            SafeArea(
                content=login_interface,
                expand=True,
            )

        )
        page.update()


    flet.app(target=main)  # view=flet.WEB_BROWSER
