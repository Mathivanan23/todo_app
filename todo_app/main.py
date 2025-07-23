import json
import os

FILE = "todo.json"

def load_tasks():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def add_task(tasks):
    task = input("Enter task: ")
    tasks.append({"task": task, "done": False})
    save_tasks(tasks)
    print("Task added.")

def view_tasks(tasks):
    if not tasks:
        print("No tasks.")
    for idx, task in enumerate(tasks, 1):
        status = "✅" if task["done"] else "❌"
        print(f"{idx}. {task['task']} [{status}]")

def mark_complete(tasks):
    view_tasks(tasks)
    index = int(input("Enter task number to mark complete: ")) - 1
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
        save_tasks(tasks)
        print("Task marked complete.")

def delete_task(tasks):
    view_tasks(tasks)
    index = int(input("Enter task number to delete: ")) - 1
    if 0 <= index < len(tasks):
        tasks.pop(index)
        save_tasks(tasks)
        print("Task deleted.")

def main():
    tasks = load_tasks()
    while True:
        print("\n--- To-Do App ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Complete")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_complete(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()