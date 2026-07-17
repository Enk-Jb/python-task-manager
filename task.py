from datetime import date
import json

tasks_list = []

print("        ***********************\n"
      "            Task Manager\n"
      "        ***********************")


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
    print("        Main Menu\n")
    print(" .Show options            [1]\n")
    print(" .Add task                [2]\n")
    print(" .View tasks              [3]\n")
    print(" .View pending tasks      [4]\n")
    print(" .View completed tasks    [5]\n")
    print(" .Remove task             [6]\n")
    print(" .Mark task as completed  [7]\n")
    print(" .Edit task               [8]\n")
    print(" .Save tasks              [9]\n")
    print(" .Exit                    [10]\n")


def add_task():
    print("\n======Add Task======\n")
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
    print("\n======View Task======\n")
    print(f"total tasks: [{len(tasks_list)}]")
    for index, task in enumerate(tasks_list, 1):
        status = "[✓]" if task.get("completed") else "[ ]"
        tdate = task.get("date")
        name = task.get("title")
        print(f"{status} {index}.{name}| {tdate}")


def display_tasks():
    if not tasks_list:
        print("No task available.")
        return
    for index, task in enumerate(tasks_list, 1):
        status = "[✓]" if task.get("completed") else "[ ]"
        tdate = task.get("date")
        name = task.get("title")
        print(f"{status} {index}.{name}| {tdate}")


def pending_tasks():
    if not tasks_list:
        print("No task available.")
        return
    print("\n======Pending Tasks======\n")
    for index, task in enumerate(tasks_list, 1):
        tdate = task.get("date")
        name = task.get("title")
        if task["completed"] is False:
            status = "Pending"
            print(f"{index}.{name}| {tdate}: [{status}]")


def completed_tasks():
    if not tasks_list:
        print("No task available.")
        return
    print("\n======Completed Tasks======\n")

    for index, task in enumerate(tasks_list, 1):
        tdate = task.get("date")
        name = task.get("title")
        if task["completed"] is True:
            status = "[✓]"
            print(f"{status} {index}.{name}| {tdate}(completed)")


def edit_task():
    if not tasks_list:
        print("No task available.")
        return
    print("\n======Edit Task======\n")
    display_tasks()

    try:
        edit_index = int(input("Task number to edit: "))
    except ValueError:
        print("\nInvalid input. Please enter a valid number.")
        return

    if edit_index == 0:
        print("task number can not be '0'")
    elif 1 <= edit_index <= len(tasks_list):
        task = tasks_list[edit_index-1]
        print(f"Task {edit_index}: [{task['title']}]")
        editor = input("Update: ")
        if editor:
            task["title"] = editor
            print("Task updated successfully")
        else:
            print("New title can not be empty.")
    else:
        print(
            f"Invalid task number. Task number "
            f"must be between 1-{len(tasks_list)}."
        )


def remove_task():
    if not tasks_list:
        print("No task available")
        return
    print("\n======Remove Task======\n")
    display_tasks()

    try:
        index = int(input("\nTask number to remove: "))
    except ValueError:
        print("\nInvalid input. Please enter a valid number.")
        return

    if index == 0:
        print("Task number cannot be '0'.")
    elif index > 0 and index <= len(tasks_list):
        removed_task = tasks_list.pop(index - 1)
        print(f"'{removed_task['title']}' has been removed.")
    else:
        print(
            f"Invalid task number. Task number "
            f"must be between 1-{len(tasks_list)}."
        )


def complete_task():
    if not tasks_list:
        print("No task available.")
        return
    print("\n======Mark Task======\n")
    display_tasks()

    try:
        completion_index = int(
            input("\nTask number to mark as completed: ").strip()
        )
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    if completion_index == 0:
        print("Task number cannot be '0'")
        return

    if 1 <= completion_index <= len(tasks_list):
        task = tasks_list[completion_index - 1]
        task["completed"] = True
        print(f"'{task['title']}' completed")
    else:
        print(
            f"Invalid task number."
            f"Task number must be between 1-{len(tasks_list)}."
        )


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
        choice = int(input("Enter your choice: "))

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
            edit_task()
        elif choice == 9:
            save()
        elif choice == 10:
            save()
            break
        else:
            print("Your choice must be between 1 and 10.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    except Exception as e:
        print(f"An error occurred: {e}")
