# Реляционные (SQL) | Нереляционные (NoSQL)

import sqlite3

from config import path_db
from db import queries



def init_db():
    conn = sqlite3.connect(path_db)     # Соединение к БД
    cursor = conn.cursor()              # Исполнитель который относит запросы к БД
    cursor.execute(queries.tasks_table)
    # cursor.execute('select * from tasks')
    conn.commit()                       # Зафиксировать измения в БД
    conn.close()                        # Закрываем соедение


def add_task(task):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()        
    cursor.execute(queries.insert_task, (task, ))
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
