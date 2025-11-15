# To-Do List Application (Console-based)

TASK_FILE = "tasks.txt"

# Load tasks from file
def load_tasks():
    try:
        with open(TASK_FILE, "r") as file:
            return [task.strip() for task in file.readlines()]
    except FileNotFoundError:
        return []

# Save tasks to file
def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def display_tasks(tasks):
    if not tasks:
        print("\nNo tasks found!")
    else:
        print("\nYour Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def add_task(tasks):
    task = input("Enter task to add: ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print("Task added successfully!")
    else:
        print("Task cannot be empty.")

def remove_task(tasks):
    display_tasks(tasks)
    try:
        task_num = int(input("Enter task number to remove: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            save_tasks(tasks)
            print(f"Removed: {removed}")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks = load_tasks()

    while True:
        print("\n--- TO-DO LIST MENU ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            display_tasks(tasks)

        elif choice == "2":
            add_task(tasks)

        elif choice == "3":
            remove_task(tasks)

        elif choice == "4":
            print("Exiting... Your tasks are saved!")
            break

        else:
            print("Invalid choice! Try again.")

if __name__== "__main__":
    main()