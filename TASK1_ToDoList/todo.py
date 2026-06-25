FILE_NAME = "tasks.txt"

print("\n" + "=" * 35)
print("      TO-DO LIST MANAGER")
print("=" * 35)

def load_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def display_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def update_task(tasks):
    if not tasks:
        print("No tasks available.")
        return

    display_tasks(tasks)

    try:
        task_num = int(input("Enter task number to update: "))

        if 1 <= task_num <= len(tasks):

            new_task = input("Enter updated task: ").strip()

            if not new_task:
                print("Task cannot be empty.")
                return

            if tasks[task_num - 1].startswith("[X]"):
                tasks[task_num - 1] = "[X] " + new_task
            else:
                tasks[task_num - 1] = "[ ] " + new_task

            save_tasks(tasks)

            print("Task updated successfully!")

        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")

def show_statistics(tasks):
    total = len(tasks)
    completed = sum(1 for task in tasks if task.startswith("[X]"))
    pending = total - completed
    if total > 0:
        percentage = (completed / total) * 100
    print("\n----- STATISTICS -----")
    print(f"Total Tasks     : {total}")
    print(f"Completed Tasks : {completed}")
    print(f"Pending Tasks   : {pending}")
    print(f"Completion Rate : {percentage:.2f}%")

tasks = load_tasks()

while True:
    print("\n------ TO-DO LIST ------")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task Completed")
    print("4. Delete Task")
    print("5. Update Task")
    print("6. View Statistics")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task: ").strip()
        if not task:
            print("Task cannot be empty!")
            continue
        tasks.append("[ ] " + task)
        if "[ ] " + task in tasks:
            print("Task already exists!")
            continue
        save_tasks(tasks)
        print("Task added successfully!")

    elif choice == "2":
        if not tasks:
            print("No tasks available.")
        else:
            display_tasks(tasks)

    elif choice == "3":
        if not tasks:
            print("No tasks available.")
        else:
            display_tasks(tasks)

            try:
                task_num = int(input("Enter task number to mark as completed: "))

                if 1 <= task_num <= len(tasks):
                    if not tasks[task_num - 1].startswith("[X]"):
                        task_text = tasks[task_num - 1]

                        if task_text.startswith("[ ]"):
                            task_text = task_text[4:]

                        tasks[task_num - 1] = "[X] " + task_text

                        save_tasks(tasks)
                        print("Task marked as completed!")
                    else:
                        print("Task already completed.")

                else:
                    print("Invalid task number.")

            except ValueError:
                print("Please enter a valid number.")
    
    elif choice == "4":
        if not tasks:
            print("No tasks available.")
        else:
            display_tasks(tasks)

            try:
                task_num = int(input("Enter task number to delete: "))

                if 1 <= task_num <= len(tasks):
                    deleted_task = tasks.pop(task_num - 1)
                    save_tasks(tasks)
                    print(f"Deleted: {deleted_task}")
                else:
                    print("Invalid task number.")

            except ValueError:
                print("Please enter a valid number.")
    
    elif choice=="5":
        update_task(tasks)
        
    elif choice=="6":
        show_statistics(tasks)

    elif choice=="7":
        print("Goodbye!")
        break
    
    else:
        print("Invalid choice.")