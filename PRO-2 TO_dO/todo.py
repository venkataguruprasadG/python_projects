tasks=[]

while True:
    print("\n Your tasks: ",tasks)

    action = input("Type add to add new tasks || 'quit' to to exit")

    if action == "add":
        task = input("Enter your task: ")
        tasks.append(task)
        print("Task is added")
    elif action == "quit":
        print("Goodbye!!!")
        break
    else:
        print("Unknown Command. Try Again")