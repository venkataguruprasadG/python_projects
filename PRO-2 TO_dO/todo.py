TASKS_FILE = "tasks.txt"

def load_tasks():
    tasks = []
    try:
        with open(TASKS_FILE, "r") as file:
            for line in file:
                tasks.append(line.strip())
    except FileNotFoundError:
        pass
    return tasks

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def main():
    tasks = load_tasks()  # tasks is defined here

    while True:
        print("\nYour tasks:")
        if not tasks:
            print("  (No tasks yet)")
        else:
            for i, task in enumerate(tasks, 1):
                print(f"  {i}. {task}")

        print("\nOptions:")
        print("  add    - Add a new task")
        print("  remove - Remove a task by its number")
        print("  quit   - Exit the app")
        action = input("What do you want to do? ")

        if action == "add":
            task = input("Enter your task: ")
            tasks.append(task)
            save_tasks(tasks)
            print("Task added!")
        elif action == "remove":
            if not tasks:
                print("No tasks to remove.")
                continue
            num = input("Enter the number of the task to remove: ")
            if num.isdigit():
                num = int(num)
                if 1 <= num <= len(tasks):
                    removed = tasks.pop(num - 1)
                    save_tasks(tasks)
                    print(f"Removed: {removed}")
                else:
                    print("Invalid task number.")
            else:
                print("Please enter a valid number.")
        elif action == "quit":
            print("Goodbye!")
            break
        else:
            print("Unknown command. Try again.")

if __name__ == "__main__":
    main()
