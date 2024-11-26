# To-Do List
to_do_list = []

while True:
    print("\nTo-Do List Options:")
    print("1. Add task")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter a new task: ")
        to_do_list.append(task)
        print("Task added.")
    elif choice == "2":
        if to_do_list:
            print("\nYour To-Do List:")
            for i, task in enumerate(to_do_list, 1):
                print(f"{i}. {task}")
        else:
            print("Your To-Do List is empty.")
    elif choice == "3":
        if to_do_list:
            print("\nYour To-Do List:")
            for i, task in enumerate(to_do_list, 1):
                print(f"{i}. {task}")
            task_num = int(input("Enter the number of the task to remove: "))
            if 1 <= task_num <= len(to_do_list):
                removed_task = to_do_list.pop(task_num - 1)
                print(f"Removed task: {removed_task}")
            else:
                print("Invalid task number.")
        else:
            print("Your To-Do List is empty.")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid option. Please try again.")
