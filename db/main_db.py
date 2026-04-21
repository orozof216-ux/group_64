import sqlite3
from config import path_db
from db import queries


def init_db():
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.tasks_table)
    conn.commit()
    conn.close()


def add_task(task):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.insert_task, (task,))
    conn.commit()
    task_id = cursor.lastrowid
    conn.close()
    return task_id


def update_task(task_id, new_task):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.update_task, (new_task, task_id))
    conn.commit()
    conn.close()


def delete_task(task_id):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()


def update_task_status(task_id, done):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET done = ? WHERE id = ?", (done, task_id))
    conn.commit()
    conn.close()


def delete_completed_tasks():
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE done = 1")
    conn.commit()
    conn.close()