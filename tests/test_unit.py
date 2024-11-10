import unittest
from models import Task, init_db
import os

class TestTaskModel(unittest.TestCase):
    def setUp(self):
        # Use a separate JSON file for testing
        self.test_data_file = 'test_tasks.json'
        global DATA_FILE
        DATA_FILE = self.test_data_file
        init_db()
        print('initialization done successfully')

    def tearDown(self):
        if os.path.exists(self.test_data_file):
            os.remove(self.test_data_file)

    def test_add_task(self):
        Task.add_task("Unit Test Task")
        tasks = Task.get_tasks()
        self.assertIn("Unit Test Task", [task['name'] for task in tasks])

    def test_add_multiple_tasks(self):
        Task.add_task("Task 1")
        Task.add_task("Task 2")
        Task.add_task('Task 3')
        tasks = Task.get_tasks()
        self.assertEqual(len(tasks), 2)
        self.assertIn("Task 1", [task['name'] for task in tasks])
        self.assertIn("Task 2", [task['name'] for task in tasks])

if __name__ == '__main__':
    unittest.main()
