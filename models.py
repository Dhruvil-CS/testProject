import json
import os
from threading import Lock

DATA_FILE = 'tasks.json'
lock = Lock()

def init_db():
    if os.path.exists(DATA_FILE):
        os.remove(DATA_FILE)  # Remove the old file if it exists
        
    # Create an empty list to represent the task data
    with open(DATA_FILE, 'w') as f:
        json.dump([], f)

class Task:
    def __init__(self, name, completed=False, task_id=None):
        self.id = task_id
        self.name = name
        self.completed = completed

    @staticmethod
    def _read_tasks():
        with lock:
            with open(DATA_FILE, 'r') as f:
                tasks_data = json.load(f)
        return tasks_data

    @staticmethod
    def _write_tasks(tasks):
        with lock:
            with open(DATA_FILE, 'w') as f:
                json.dump(tasks, f, indent=4)

    @staticmethod
    def add_task(name):
        tasks = Task._read_tasks()
        task_id = (max([task['id'] for task in tasks], default=0) + 1) if tasks else 1
        new_task = {'id': task_id, 'name': name, 'completed': False}
        tasks.append(new_task)
        Task._write_tasks(tasks)
        return True

    @staticmethod
    def get_tasks():
        tasks = Task._read_tasks()
        return tasks

    @staticmethod
    def update_task(task_id, completed):
        tasks = Task._read_tasks()
        for task in tasks:
            if task['id'] == task_id:
                task['completed'] = completed
                Task._write_tasks(tasks)
                return True
        raise ValueError(f"Task with ID {task_id} does not exist.")

    @staticmethod
    def delete_task(task_id):
        tasks = Task._read_tasks()
        updated_tasks = [task for task in tasks if task['id'] != task_id]
        if len(tasks) == len(updated_tasks):
            raise ValueError(f"Task with ID {task_id} does not exist.")
        Task._write_tasks(updated_tasks)
        return True

# Initialize the JSON database
init_db()
