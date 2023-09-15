import flet
from flet import OutlinedButton, Tabs, Tab, colors, IconButton, UserControl, CrossAxisAlignment, Row, Column, Page, \
    ElevatedButton, Text, TextField, FloatingActionButton, icons, Checkbox


class Task(UserControl):
    def __init__(self, task_name, task_status_change, task_delete):
        super().__init__()
        self.completed = False
        self.task_name = task_name
        self.task_status_change = task_status_change
        self.task_delete = task_delete

    def build(self):
        self.chk_tarea = Checkbox(value=False, label=self.task_name, on_change=self.status_changed)
        self.txt_editar_nombre = TextField(expand=1)

        self.display_view = Row(
            alignment="spaceBetween",
            vertical_alignment="center",
            controls=[
                self.chk_tarea,
                Row(
                    spacing=0,
                    controls=[
                        IconButton(
                            icon=icons.CREATE_OUTLINED,
                            tooltip="Edit To-Do",
                            on_click=self.edit_clicked
                        ),
                        IconButton(
                            icon=icons.DELETE_OUTLINE,
                            tooltip="Delete To-Do",
                            on_click=self.delete_clicked
                        )
                    ]
                )

            ]
        )

        self.edit_view = Row(
            visible=False,
            alignment="spaceBetween",
            vertical_alignment="center",
            controls=[
                self.txt_editar_nombre,
                IconButton(
                    icon=icons.DONE_OUTLINE_OUTLINED,
                    icon_color=colors.GREEN,
                    tooltip="Update To-Do",
                    on_click=self.save_clicked
                )
            ]
        )

        return Column(controls=[self.display_view, self.edit_view])

    def edit_clicked(self, event):
        self.txt_editar_nombre.value = self.chk_tarea.label
        self.display_view.visible = False
        self.edit_view.visible = True
        self.update()

    def delete_clicked(self, event):
        self.task_delete(self)

    def save_clicked(self, event):
        self.chk_tarea.label = self.txt_editar_nombre.value
        self.display_view.visible = True
        self.edit_view.visible = False
        self.update()

    def status_changed(self, event):
        self.completed = self.chk_tarea.value
        self.task_status_change(self)


class ToDoApp(UserControl):
    def build(self):
        self.txt_tarea = TextField(hint_text="¡Qué necesitas hacer¡", expand=True)
        self.btn_agregar_tarea = FloatingActionButton(icon=icons.ADD, on_click=self.btn_agregar_tarea_on_click)
        self.filter = Tabs(
            selected_index=0,
            on_change=self.tabs_changed,
            tabs=[
                Tab(text="Todo"),
                Tab(text="Activas"),
                Tab(text="Completas")
            ]
        )
        self.col_tareas = Column()

        self.items_left = Text("0 Tareas Pendientes")
        self.col_main = Column(
            width=600,
            controls=[
                Row([Text(value="To-Do App", style="headlineMedium")], alignment="center"),
                Row([
                    self.txt_tarea,
                    self.btn_agregar_tarea
                ]),
                Column(
                    spacing=25,
                    controls=[
                        self.filter,
                        self.col_tareas,
                        Row(
                            alignment="spaceBetween",
                            vertical_alignment="center",
                            controls=[
                                self.items_left,
                                OutlinedButton(
                                    text="Borrar Completas",
                                    on_click=self.clear_clicked
                                )
                            ]
                        )
                    ]
                )

            ]
        )
        return self.col_main

    def clear_clicked(self, event):
        for task in self.col_tareas.controls[:]:
            if task.completed:
                self.task_delete(task)

    def btn_agregar_tarea_on_click(self, event):
        task = Task(self.txt_tarea.value, self.task_status_change, self.task_delete)
        self.col_tareas.controls.append(task)
        self.txt_tarea.value = ""
        self.update()

    def task_delete(self, task):
        self.col_tareas.controls.remove(task)
        self.update()

    def task_status_change(self, task):
        self.update()

    def tabs_changed(self, event):
        self.update()

    def update(self):
        status = self.filter.tabs[self.filter.selected_index].text
        count = 0
        for task in self.col_tareas.controls:
            task.visible = (
                    status == "Todo"
                    or (status == "Activas" and task.completed == False)
                    or (status == "Completas" and task.completed)
            )
            if not task.completed:
                count += 1
        self.items_left.value = f"{count} Tarea(s) Pendiente"

        super().update()


def main(page: Page):
    page.title = "ToDo App"
    page.horizontal_alignment = CrossAxisAlignment.CENTER

    ToDo = ToDoApp()

    page.add(
        ToDo
    )


flet.app(target=main)
