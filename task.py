from datetime import date

tasks_list = []

print("======Task Manager======")


def options():
    print("options:")
    print("1. show options")
    print("2. Add task")
    print("3. Show tasks")
    print("4. remove task")
    print("5. mark task as completed")
    print("6. Exit")


def add_task():
    title = input("add a task : ").strip()
    if title:
        tasks_list.append({"title": title, "completed": False, "date": date.today()})
        print(f"Task '{title}' has been added.")
    else:
        print("Task cannot be empty. please enter a valid task.")


def show_tasks():

    if not tasks_list:
        print("No task available.")
        return
    for index, task in enumerate(tasks_list, 1):
        status = "[✓]" if task.get("completed") else "[ ]"
        tdate = task.get("date")
        name = task.get("title")
        print(f"{status} {index}.{name}|{tdate}")


def remove_task():
    show_tasks()
    if not tasks_list:
        return

    try:
        index = int(input("Enter the task number to remove: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    if index == 0:
        print("Task number cannot be zero.")
    elif index > 0 and index <= len(tasks_list):
        removed_task = tasks_list.pop(index - 1)
        print(f"Task '{removed_task['title']}' has been removed.")
    else:
        print(f"Invalid task number. Task number "
              f"must be between 1-{len(tasks_list)}.")


def complete_task():
    show_tasks()
    if not tasks_list:
        print("No task available.")
        return

    try:
        completion_index = int(input("Enter the task number to mark as completed: ").strip())
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    if completion_index == 0:
        print("Task number cannot be zero")
        return

    if 1 <= completion_index <= len(tasks_list):
        task = tasks_list[completion_index - 1]
        task["completed"] = True
        print(f"'{task['title']}' completed")
    else:
        print(f"Invalid task number. Task number must be between 1-{len(tasks_list)}.")


options()

while True:
    try:
        choice = int(input("Please make a choice: "))

        if choice == 1:
            options()
        elif choice == 2:
            add_task()
        elif choice == 3:
            show_tasks()
        elif choice == 4:
            remove_task()
        elif choice == 5:
            complete_task()
        elif choice == 6:
            break
        else:
            print("Invalid choice. Please make a choice between 1 and 6.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    except Exception as e:
        print(f"An error occurred: {e}")
