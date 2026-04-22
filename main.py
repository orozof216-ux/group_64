import flet as ft
from db import main_db 


def main(page: ft.Page):
    page.title = "Список покупок"
    page.theme_mode = ft.ThemeMode.LIGHT

    task_list = ft.Column()
    filter_type = 'all'

    def load_tasks():
        task_list.controls.clear()
        tasks = main_db.get_tasks(filter_type=filter_type)

        for task_id, task_text, completed in tasks:
            task_list.controls.append(
                view_tasks(task_id, task_text, completed)
            )

        page.update()   # 🔥 важно!

    def view_tasks(task_id, task_text, completed=0):
        checkbox = ft.Checkbox(
            value=bool(completed),
            on_change=lambda e, id=task_id: toggle_task(id, e.control.value)
        )

        task_field = ft.TextField(
            read_only=True,
            value=task_text,
            expand=True
        )

        def enable_edit(e):
            task_field.read_only = not task_field.read_only
            page.update()

        edit_button = ft.IconButton(
            icon=ft.Icons.EDIT,
            on_click=enable_edit
        )

        def save_task(e):
            main_db.update_task(task_id=task_id, new_task=task_field.value)
            task_field.read_only = True
            page.update()

        save_button = ft.IconButton(
            icon=ft.Icons.SAVE,
            on_click=save_task
        )

        def delete_task(e):
            main_db.delete_task(task_id)
            load_tasks()

        delete_button = ft.IconButton(
            icon=ft.Icons.DELETE,
            on_click=delete_task
        )

        return ft.Row([checkbox, task_field, edit_button, save_button, delete_button])

    def toggle_task(task_id, is_completed):
        main_db.update_task(task_id=task_id, completed=int(is_completed))
        load_tasks()

    def add_task(e):
        if task_input.value:
            task = task_input.value

            task_id = main_db.add_task(task=task)

            task_input.value = ""
            load_tasks()   # 🔥 обновляем список

    task_input = ft.TextField(
        label="Введите задачу",
        expand=True,
        on_submit=add_task
    )

    task_button = ft.IconButton(
        icon=ft.Icons.ADD,
        on_click=add_task
    )

    def set_filter(filter_value):
        nonlocal filter_type
        filter_type = filter_value
        load_tasks()

    filter_buttons = ft.Row([
        ft.ElevatedButton(
            'Все',
            on_click=lambda e: set_filter('all')
        ),
        ft.ElevatedButton(
            'В работе',
            on_click=lambda e: set_filter('uncompleted')
        ),
        ft.ElevatedButton(
            'Готово',
            on_click=lambda e: set_filter('completed')
        )
    ])

    page.add(
        ft.Row([task_input, task_button]),
        filter_buttons,
        task_list
    )

    load_tasks()


if __name__ == "__main__":
    main_db.init_db()
    ft.app(target=main)