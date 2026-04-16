# C - R - U - D


tasks_table = """
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task TEXT NOT NULL
    )
"""


# Create - создание записи

insert_task = 'INSERT INTO tasks (task) VALUES (?)'


# Read - Просмотр записи
select_tasks = 'SELECT * FROM tasks'


# Update - Обновить запись
update_task = 'UPDATE tasks SET task = ? WHERE id = ?'


# Delete - Удаление записи
delete_task = 'DELETE FROM tasks WHERE id = ?'