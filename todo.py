# todo.py
# Simple command-line to-do list app

tasks = []

def add_task(task):
    """Add a task to the list."""
    # Fill in: Append task to the tasks list
    pass

def view_tasks():
    """View all tasks."""
    # Fill in: Print all tasks in the tasks list
    pass

def complete_task(task_number):
    """Mark a task as complete by its index."""
    # Fill in: Mark the task as completed (could just remove or indicate it)
    pass

def remove_task(task_number):
    """Remove a task from the list by its index."""
    # Fill in: Remove the task from the tasks list
    pass

if __name__ == "__main__":
    while True:
        print("\nTo-Do List")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Remove Task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            task = input("Enter a new task: ")
            add_task(task)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            task_number = int(input("Enter task number to complete: "))
            complete_task(task_number)
        elif choice == '4':
            task_number = int(input("Enter task number to remove: "))
            remove_task(task_number)
        elif choice == '5':
            break
        else:
            print("Invalid option, please try again.")
