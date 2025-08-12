def task():
    tasks = []
    print("____WELCOME TO THE TASK MANAGEMENT APP____")

    total_task = int(input('Enter how many tasks you want to add: '))
    for i in range(1, total_task + 1):
        task_name = input(f'Enter task {i}: ')
        tasks.append(task_name)

    print(f"\nToday's tasks are:\n{tasks}\n")

    while True:
        operation = int(input("\nEnter your choice:\n1-Add\n2-Update\n3-Delete\n4-View\n5-Exit\nChoice: "))

        if operation == 1:
            add = input("Enter task you want to add: ")
            tasks.append(add)
            print(f'Task "{add}" has been successfully added.')

        elif operation == 2:
            updated_val = input("Enter the task name you want to update: ")
            if updated_val in tasks:
                new_task = input("Enter new task: ")
                ind = tasks.index(updated_val)
                tasks[ind] = new_task
                print(f'Task updated to "{new_task}"')
            else:
                print("Task not found.")

        elif operation == 3:
            del_val = input("Which task do you want to delete: ")
            if del_val in tasks:
                tasks.remove(del_val)
                print(f'The task "{del_val}" has been deleted.')
            else:
                print("Task not found.")

        elif operation == 4:
            print(f'Total tasks: {tasks}')

        elif operation == 5:
            print("Closing the program...")
            break

        else:
            print("Invalid input. Please try again.")

# Call the function to run it
task()
