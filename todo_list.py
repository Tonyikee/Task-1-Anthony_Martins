todo_list = []


def add_task():
    task = input("Enter a Task: ")
    todo_list.append({"Task": task, "status": "pending"})
    print("New Task Added Susccessfully!\n")


def view_task():
    print("Your Todo list: ")
    if len(todo_list) == 0:
        print("No pending taskes\n")
    else:
        for index, task in enumerate(todo_list, 1):
            print(f"{index}: {task['Task']} - {task['status']}")
    print("\n")


def remove_task():
    if len(todo_list) == 0:
        print("List is Empty!\n")
    else:
        try:
            search_index = int(
                input("Enter the task number that you want to remove: ")) - 1
            if 0 <= search_index < len(todo_list):
                removed_task = todo_list.pop(search_index)
                print(f"Task Removed Successfully: {removed_task['Task']}\n")
            else:
                print("Invalid Task Number! Try Again!!!\n")
        except ValueError:
            print("Please enter a valid task number!\n")


def mark_done():
    if len(todo_list) == 0:
        print("List is Empty!\n")
    else:
        try:
            search_index = int(
                input("Enter the task number you want to mark as complete:")) - 1
            if 0 <= search_index < len(todo_list):
                todo_list[search_index]['status'] = "Done"
                print(
                    f"Task {todo_list[search_index]['Task']} has been marked as done.\n")

            else:
                print("Invalid Task Number! Try Again!!!\n")
        except ValueError:
            print("Please enter a valid task number!\n")


def menu():
    while (True):
        print("*** Main Menu ***")
        print("1. Add a New Task")
        print("2. View All Tasks")
        print("3. Remove a Task")
        print("4. Mark a Task as Completed")
        print("5. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            add_task()

        elif choice == "2":
            view_task()

        elif choice == "3":
            remove_task()

        elif choice == "4":
            mark_done()

        elif choice == "5":
            print("Exkting the application...\n")
            exit()

        else:
            print("invalid choice! Try again!!!\n")


menu()
