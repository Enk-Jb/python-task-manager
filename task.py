from datetime import date
import json

tasks_list = []

print("======Task Manager======")


def load():
    try:
        with open("data.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            tasks_list.extend(data)

            for task in tasks_list:
                task["date"] = date.fromisoformat(task["date"])

    except FileNotFoundError:
        print("No task saved")


def options():
    print("options:")
    print("1. show options")
    print("2. Add task")
    print("3. View tasks")
    print("4. View pending tasks")
    print("5. View completed tasks")
    print("6. remove task")
    print("7. mark task as completed")
    print("8. Save tasks")
    print("9. Exit")


def add_task():
    title = input("add a task : ").strip()
    if title:
        tasks_list.append({"title": title, "completed": False,
                           "date": date.today()})
        print(f"Task '{title}' has been added.")
    else:
        print("Task cannot be empty. please enter a valid task.")


def view_tasks():

    if not tasks_list:
        print("No task available.")
        return
    for index, task in enumerate(tasks_list, 1):
        status = "[✓]" if task.get("completed") else "[ ]"
        tdate = task.get("date")
        name = task.get("title")
        print(f"{status} {index}.{name}|{tdate}")


def pending_tasks():
    if not tasks_list:
        print("No task available.")
        return
    for index, task in enumerate(tasks_list, 1):
        tdate = task.get("date")
        name = task.get("title")
        if task["completed"] is False:
            status = "Pending"
            print(f"{index}.{name}|{tdate}: {status}")


def completed_tasks():
    if not tasks_list:
        print("No task available.")
        return

    for index, task in enumerate(tasks_list, 1):
        tdate = task.get("date")
        name = task.get("title")
        if task["completed"] is True:
            status = "[✓]"
            print(f"{status} {index}.{name}|{tdate}(completed)")


def remove_task():
    view_tasks()
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
        print(
            f"Invalid task number. Task number "
            f"must be between 1-{len(tasks_list)}."
        )


def complete_task():
    view_tasks()
    if not tasks_list:
        print("No task available.")
        return

    try:
        completion_index = int(
            input("Enter the task number to mark as completed: ").strip()
        )
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
        print(f"Invalid task number."
              f"Task number must be between 1-{len(tasks_list)}.")


def save():
    data_to_save = []

    for task in tasks_list:
        task_copy = task.copy()

        if isinstance(task_copy["date"], date):
            task_copy["date"] = task_copy["date"].isoformat()

        data_to_save.append(task_copy)

    with open("data.json", "w", encoding="utf-8") as file:
        json.dump(data_to_save, file, indent=4)

    print("Tasks saved successfully.")


load()
options()


while True:
    try:
        choice = int(input("Please make a choice: "))

        if choice == 1:
            options()
        elif choice == 2:
            add_task()
        elif choice == 3:
            view_tasks()
        elif choice == 4:
            pending_tasks()
        elif choice == 5:
            completed_tasks()
        elif choice == 6:
            remove_task()
        elif choice == 7:
            complete_task()
        elif choice == 8:
            save()
        elif choice == 9:
            save()
            break
        else:
            print("Invalid choice. Please make a choice between 1 and 9.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    except Exception as e:
        print(f"An error occurred: {e}")
