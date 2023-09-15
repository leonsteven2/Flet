import flet
from flet import IconButton, Page, Row, TextField, icons, ProgressRing, Column, CircleAvatar

def main(page: Page):
    page.add(Column(controls=[Row(controls=[ProgressRing(color="red",bgcolor="black"),CircleAvatar(radius=None, foreground_image_url="https://avatars.githubusercontent.com/u/5041459?s=88&v=4",width=300,height=300)], alignment="center")],alignment="center"))

flet.app(target=main)

