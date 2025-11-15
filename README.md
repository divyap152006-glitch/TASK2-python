# TASK2-python
# To-Do List Application (Console-Based)

This is a simple Python console-based To-Do List application that allows
you to add, view, and remove tasks. All tasks are stored in a text file
(`tasks.txt`) so that they persist even after closing the program.

------------------------------------------------------------------------

## \## Features

-   Add new tasks
-   View existing tasks
-   Remove tasks by selecting task number
-   Auto-save tasks to `tasks.txt`
-   Loads tasks automatically on startup

------------------------------------------------------------------------

## \## How It Works

### 1. **Loading Tasks**

The program loads all tasks from a file named **tasks.txt**.\
If the file doesn't exist, it creates a new one when tasks are saved.

### 2. **Viewing Tasks**

Displays all saved tasks with numbering for easy management.

### 3. **Adding a Task**

-   User enters a task description.
-   Task is added to the list and saved to the file.

### 4. **Removing a Task**

-   Shows all tasks.
-   User selects the task number to remove.
-   The task is deleted and changes are saved.

### 5. **Exiting**

The program exits safely after saving all tasks.

------------------------------------------------------------------------

## \## How to Run

1.  Make sure you have **Python installed**.
2.  Save the script as `todo.py`.
3.  Run the program in terminal:

```{=html}
<!-- -->
```
    python todo.py

4.  The menu will appear, and you can start managing your tasks!

------------------------------------------------------------------------

## \## File Structure

    todo.py
    tasks.txt   (automatically created after first task is added)

------------------------------------------------------------------------

## \## Requirements

-   Python 3.x

------------------------------------------------------------------------

## \## License

This project is free to use for learning and personal projects.
