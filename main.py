import flet as ft
from db import main_db 


def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT

    task_list = ft.Column()

    def view_tasks(task_id, task_text):
        task_field = ft.TextField(read_only=True, value=task_text, expand=True)

        def enable_edit(e):
            task_field.read_only = not task_field.read_only

        edit_button = ft.IconButton(icon=ft.Icons.EDIT, on_click=enable_edit)

        def save_task(e):
            main_db.update_task(task_id=task_id, new_task=task_field.value)
            task_field.read_only = True

        save_button = ft.IconButton(icon=ft.Icons.SAVE, on_click=save_task)

        def delete_task_click(e):
            main_db.delete_task(task_id)
            task_list.controls.remove(task_row)
            page.update()

        delete_button = ft.IconButton(icon=ft.Icons.DELETE, on_click=delete_task_click)

        task_row = ft.Row([task_field, edit_button, save_button, delete_button])

        return task_row

    def add_task(e):
        if task_input.value:
            task = task_input.value
            task_id = main_db.add_task(task=task)
            print(f'Задача {task} добавлена! Его ID - {task_id}')
            task_list.controls.append(view_tasks(task_id=task_id, task_text=task))
            task_input.value = None
            page.update()

    task_input = ft.TextField(label="Введите задачу", expand=True, on_submit=add_task)

    task_button = ft.IconButton(icon=ft.Icons.ADD, on_click=add_task)

    send_task = ft.Row([task_input, task_button])

    page.add(send_task, task_list)


if __name__ == "__main__":
    main_db.init_db()
    ft.run(main, view=ft.AppView.WEB_BROWSER)
    