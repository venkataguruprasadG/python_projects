tasks=[]

while True:
    print("\n Your tasks: ",tasks)

    if not tasks:
        print("No tasks yet..!!")
    else:
        for i, task in enumerate(tasks, 1):
            print(f" {i}. {task}")
    
    print("\nOptions: ")
    print("Type 'add' to add a new task")
    print("Type 'Remove' to remove a task")
    print("Type 'quit' to quit from the app")

    action = input("Type about the task what you want to do ?")
    
    if action == "add":
        task = input("Enter your task: ")
        tasks.append(task)
        print("Task is added")
    elif action == "remove":
        if not tasks:
            print("No tasks to remove")
            continue
        num = input("Enter the number of the task you want to remove: ")
        if num.isdigit():
            num = int(num)
            if 1<= num <= len(tasks):
                removed = tasks.pop(num-1)
            else:
                print("Invalid Task Number: ",num)
        else:
            print("Enter the valid task number")
    elif action == "quit":
        print("Goodbye!!!")
        break
    else:
        print("Unknown Command. Try Again")