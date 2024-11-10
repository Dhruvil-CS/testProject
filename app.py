from models import Task

def show_menu():
    print("\nTo-Do List CLI Application")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

def main():
    while True:
        show_menu()
        choice = input("Choose an option: ")
        
        if choice == '1':
            name = input("Enter task name: ")
            Task.add_task(name)
            print(f"Task '{name}' added.")
        
        elif choice == '2':
            tasks = Task.get_tasks()
            print("\nTasks:")
            for task in tasks:
                status = "Completed" if task['completed'] else "Pending"
                print(f"{task['id']}: {task['name']} - {status}")
        
        elif choice == '3':
            try:
                task_id = int(input("Enter task ID to update: "))
                completed_input = input("Mark as completed? (y/n): ").lower()
                if completed_input not in ['y', 'n']:
                    print("Invalid input for completion status. Please enter 'y' or 'n'.")
                    continue
                completed = completed_input == 'y'
                Task.update_task(task_id, completed)
                print(f"Task {task_id} updated.")
            except ValueError as ve:
                print(f"Error: {ve}")
        
        elif choice == '4':
            try:
                task_id = int(input("Enter task ID to delete: "))
                Task.delete_task(task_id)
                print(f"Task {task_id} deleted.")
            except ValueError as ve:
                print(f"Error: {ve}")
        
        elif choice == '5':
            print("Exiting application.")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
