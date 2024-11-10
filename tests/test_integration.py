import unittest
from models import Task, init_db
import os

class TestIntegration(unittest.TestCase):
    def setUp(self):
        # Use a separate JSON file for testing
        self.test_data_file = 'test_tasks.json'
        global DATA_FILE
        DATA_FILE = self.test_data_file
        init_db()

    def tearDown(self):
        if os.path.exists(self.test_data_file):
            os.remove(self.test_data_file)

    def test_create_and_update_task(self):
        Task.add_task("Integration Test Task")
        tasks = Task.get_tasks()
        self.assertEqual(len(tasks), 1)
        task_id = tasks[0]['id']
        
        Task.update_task(task_id, True)
        updated_task = [task for task in Task.get_tasks() if task['id'] == task_id][0]
        self.assertTrue(updated_task['completed'])

    def test_delete_task(self):
        Task.add_task("Task to Delete")
        tasks = Task.get_tasks()
        task_id = tasks[0]['id']
        
        Task.delete_task(task_id)
        tasks_after_delete = Task.get_tasks()
        self.assertEqual(len(tasks_after_delete), 0)

    def test_update_nonexistent_task(self):
        with self.assertRaises(ValueError):
            Task.update_task(999, True)

    def test_delete_nonexistent_task(self):
        with self.assertRaises(ValueError):
            Task.delete_task(999)

if __name__ == '__main__':
    unittest.main()
