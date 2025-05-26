import os

TASKS_FILE = "tasks.txt"

def load_tasks():
    tasks = []
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            for line in file:
                # Each line: description|||priority
                parts = line.strip().split("|||")
                if len(parts) == 2:
                    task = {"desc": parts[0], "priority": parts[1]}
                    tasks.append(task)
    return tasks

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(f"{task['desc']}|||{task['priority']}\n")

def main():
    tasks = load_tasks()

    while True:
        print("\nYour tasks:")
        if not tasks:
            print("  (No tasks yet)")
        else:
            # Sort by priority (High, Medium, Low)
            priority_order = {"High": 1, "Medium": 2, "Low": 3}
            tasks_sorted = sorted(tasks, key=lambda t: priority_order.get(t["priority"], 4))
            for i, task in enumerate(tasks_sorted, 1):
                print(f"  {i}. [{task['priority']}] {task['desc']}")

        print("\nOptions:")
        print("  add    - Add a new task")
        print("  remove - Remove a task by its number")
        print("  quit   - Exit the app")
        action = input("What do you want to do? ")

        if action == "add":
            desc = input("Enter your task: ")
            priority = input("Priority (High/Medium/Low): ").capitalize()
            if priority not in ["High", "Medium", "Low"]:
                print("Invalid priority. Defaulting to 'Low'.")
                priority = "Low"
            tasks.append({"desc": desc, "priority": priority})
            save_tasks(tasks)
            print("Task added!")
        elif action == "remove":
            if not tasks:
                print("No tasks to remove.")
                continue
            num = input("Enter the number of the task to remove: ")
            if num.isdigit():
                num = int(num)
                # Remove from the sorted list, so find the right index in the original list
                priority_order = {"High": 1, "Medium": 2, "Low": 3}
                tasks_sorted = sorted(tasks, key=lambda t: priority_order.get(t["priority"], 4))
                if 1 <= num <= len(tasks_sorted):
                    removed_task = tasks_sorted[num - 1]
                    tasks.remove(removed_task)
                    save_tasks(tasks)
                    print(f"Removed: [{removed_task['priority']}] {removed_task['desc']}")
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
