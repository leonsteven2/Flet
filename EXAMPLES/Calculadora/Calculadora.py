import flet
from flet import UserControl, Page, Text, ElevatedButton, Row, Column, Container, border_radius, colors


class CalculatorApp(UserControl):
    def build(self):
        self.reset()
        self.lbl_resultado = Text(value="0", color=colors.WHITE, size=20)

        Container1 = Container(
            width=350,
            bgcolor=colors.BLACK,
            border_radius=border_radius.all(20),
            padding=20,
            content=Column(
                controls=[
                    Row(controls=[self.lbl_resultado], alignment="end"),
                    Row(
                        controls=[
                            ElevatedButton(
                                text="AC",
                                bgcolor=colors.BLUE_GREY_100,
                                color=colors.BLACK,
                                expand=1,
                                on_click=self.button_clicked,
                                data="AC"
                            ),
                            ElevatedButton(
                                text="+/-",
                                bgcolor=colors.BLUE_GREY_100,
                                color=colors.BLACK,
                                expand=1,
                                on_click=self.button_clicked,
                                data="+/-"
                            ),
                            ElevatedButton(
                                text="%",
                                bgcolor=colors.BLUE_GREY_100,
                                color=colors.BLACK,
                                expand=1,
                                on_click=self.button_clicked,
                                data="%"
                            ),
                            ElevatedButton(
                                text="/",
                                bgcolor=colors.ORANGE,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data="/"
                            ),
                        ]
                    ),
                    Row(
                        controls=[
                            ElevatedButton(
                                text="7",
                                bgcolor=colors.WHITE24,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data="7"
                            ),
                            ElevatedButton(
                                text="8",
                                bgcolor=colors.WHITE24,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data="8"
                            ),
                            ElevatedButton(
                                text="9",
                                bgcolor=colors.WHITE24,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data="9"
                            ),
                            ElevatedButton(
                                text="*",
                                bgcolor=colors.ORANGE,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data="*"
                            ),
                        ]
                    ),
                    Row(
                        controls=[
                            ElevatedButton(
                                text="4",
                                bgcolor=colors.WHITE24,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data="4"
                            ),
                            ElevatedButton(
                                text="5",
                                bgcolor=colors.WHITE24,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data="5"
                            ),
                            ElevatedButton(
                                text="6",
                                bgcolor=colors.WHITE24,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data="6"
                            ),
                            ElevatedButton(
                                text="-",
                                bgcolor=colors.ORANGE,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data="-"
                            ),
                        ]
                    ),
                    Row(
                        controls=[
                            ElevatedButton(
                                text="1",
                                bgcolor=colors.WHITE24,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data="1"
                            ),
                            ElevatedButton(
                                text="2",
                                bgcolor=colors.WHITE24,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data="2"
                            ),
                            ElevatedButton(
                                text="3",
                                bgcolor=colors.WHITE24,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data="3"
                            ),
                            ElevatedButton(
                                text="+",
                                bgcolor=colors.ORANGE,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data="+"
                            ),
                        ]
                    ),
                    Row(
                        controls=[
                            ElevatedButton(
                                text="0",
                                bgcolor=colors.WHITE24,
                                color=colors.WHITE,
                                expand=2,
                                on_click=self.button_clicked,
                                data="0"
                            ),
                            ElevatedButton(
                                text=".",
                                bgcolor=colors.WHITE24,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data="."
                            ),
                            ElevatedButton(
                                text="=",
                                bgcolor=colors.ORANGE,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data="="
                            )
                        ]
                    )

                ]
            )
        )
        return Container1

    def button_clicked(self, event):
        print("Hola mundo")
        data = event.control.data  # Trae el valor de la tecla presionada

        if self.lbl_resultado.value == "Error" or data == "AC":
            self.lbl_resultado.value = "0"
            self.reset()


        elif data in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "."):
            if self.lbl_resultado.value == "0" or self.new_operand == True:
                self.lbl_resultado.value = data
                self.new_operand = False
            else:
                self.lbl_resultado.value = self.lbl_resultado.value + data

        elif data in ("+", "-", "*", "/"):
            self.lbl_resultado.value = self.calculate(
                self.operand1, float(self.lbl_resultado.value), self.operator
            )
            self.operator = data
            if self.lbl_resultado.value == "Error":
                self.operand1 = "0"
            else:
                self.operand1 = float(self.lbl_resultado.value)
            self.new_operand = True

        elif data in "=":
            self.lbl_resultado.value = self.calculate(
                self.operand1, float(self.lbl_resultado.value), self.operator
            )
            self.reset()

        elif event.data == "%":
            self.lbl_resultado.value = float(self.lbl_resultado.value) / 100
            self.reset()

        elif event.data == '+/-':
            if float(self.lbl_resultado.value) > 0:
                self.lbl_resultado.value = "-" + str(self.lbl_resultado.value)

            elif float(self.lbl_resultado.value) < 0:
                self.lbl_resultado.value = str(
                    self.format_number(abs(float(self.lbl_resultado.value)))
                )

        self.update()

    def reset(self):
        self.operator = "+"
        self.operand1 = 0
        self.new_operand = True

    def format_number(self, num):
        if num % 1 == 0:
            return int(num)
        else:
            return num

    def calculate(self, operand1, operand2, operator):
        if operator == "+":
            return self.format_number(operand1 + operand2)
        elif operator == "-":
            return self.format_number(operand1 - operand2)
        elif operator == "*":
            return self.format_number(operand1 * operand2)
        elif operator == "/":
            if operand2 == 0:
                return "Error"
            else:
                return self.format_number(operand1 / operand2)


def main(page: Page):
    page.title = "Calculadora App"
    page.bgcolor = "green"

    calculadora = CalculatorApp()

    page.add(
        calculadora,
    )


flet.app(target=main)
