import flet
import time
from flet import Page, Image, AnimatedSwitcher, ElevatedButton


def main(page: Page):
    image = Image(src="https://picsum.photos/150/150", width=150, height=150)

    def animate(event):
        switch.content = Image(src=f'https://picsum.photos/150/150?{time.time()}', width=150)
        page.update()

    switch = AnimatedSwitcher(
        image,
        transition="scale",
        duration=500,
        reverse_duration=500,
        switch_in_curve="bounceOut",
        switch_out_curve="bounceIn",

    )

    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    page.spacing = 30

    page.add(
        switch,
        ElevatedButton("Animate!", on_click=animate)
    )

flet.app(target=main)