import unittest
from models import Task, init_db
import os

class TestEndToEnd(unittest.TestCase):
    def setUp(self):
        # Use a separate JSON file for testing
        self.test_data_file = 'test_tasks.json'
        global DATA_FILE
        DATA_FILE = self.test_data_file
        init_db()

    def tearDown(self):
        if os.path.exists(self.test_data_file):
            os.remove(self.test_data_file)

    def test_full_workflow(self):
        # Create a task
        Task.add_task("E2E Test Task")
        tasks = Task.get_tasks()
        self.assertEqual(len(tasks), 1)
        task_id = tasks[0]['id']
        
        # Update the task
        Task.update_task(task_id, True)
        updated_task = [task for task in Task.get_tasks() if task['id'] == task_id][0]
        self.assertTrue(updated_task['completed'])
        
        # Delete the task
        Task.delete_task(task_id)
        tasks_after_delete = Task.get_tasks()
        self.assertEqual(len(tasks_after_delete), 0)

if __name__ == '__main__':
    unittest.main()
