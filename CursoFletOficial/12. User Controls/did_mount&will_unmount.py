import flet
from flet import Page, Text, UserControl
import time
from threading import Thread

class Countdown(UserControl):
    def __init__(self, seconds):
        super().__init__()
        self.seconds = seconds

    def did_mount(self):
        self.running = True
        self.hilo = Thread(target=self.update_timer, args=(), daemon=True)
        self.hilo.start()

    def will_unmount(self):
        self.running = False

    def update_timer(self):
        while self.seconds+1 and self.running:
            mins, secs = divmod(self.seconds, 60) #divmod nos entrega el cociente y el residuo, el 60 determina que 1 min equivale a 60 segundos
            self.countdown.value = "{:02d}:{:02d}".format(mins,secs)
            self.update()
            time.sleep(1)
            self.seconds -= 1

    def build(self):
        self.countdown = Text()
        return self.countdown

def main(page: Page):
    page.add(Countdown(5), Countdown(7))

flet.app(target=main)