import os
from datetime import datetime

print("RUNNING THIS FILE") 

# main.py
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "tasks.txt")

# Load tasks
tasks = []

try:
    with open(FILE_PATH, "r") as file:
        tasks = file.read().splitlines()
except FileNotFoundError:
    tasks = []


# Save tasks
def save_tasks():
    with open(FILE_PATH, "w") as file:
        for task in tasks:
            file.write(task + "\n")


# Main loop
while True:

    print("\n====================")
    print("     TO-DO APP")
    print("====================")

    print("\n1. Show tasks")
    print("2. Add task")
    print("3. Delete task")
    print("4. Edit task")
    print("5. Exit")

    choice = input("\nChoose: ").strip()

    # Show tasks
    if choice == "1":
        if not tasks:
            print("No tasks")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks):
                print(f"{i+1}. {task}")

        input("\nPress Enter...")

    # Add task
    elif choice == "2":
        newtask = input("Enter task: ").strip()

        if newtask == "":
            print("Task cannot be empty")

        else:
            # Avoid repetition (raw noun only)
            clean_tasks = [t.split(" (")[0] for t in tasks]

            if newtask in clean_tasks:
                print("Task already exists!")
            else:
                task_with_date = f"{newtask} (added: {datetime.now().strftime('%Y-%m-%d')})"
                tasks.append(task_with_date)
                save_tasks()
                print("Task added!")

        input("\nPress Enter...")

    # Delete task
    elif choice == "3":
        if not tasks:
            print("No tasks to delete")

        else:
            for i, task in enumerate(tasks):
                print(f"{i+1}. {task}")

            try:
                num = int(input("Enter task number: "))

                if 0 < num <= len(tasks):
                    removed = tasks.pop(num - 1)
                    save_tasks()
                    print(f"Deleted: {removed}")
                else:
                    print("Invalid number")

            except ValueError:
                print("Invalid input")

        input("\nPress Enter...")

    #Edit Task 
    elif choice == "4":
        if not tasks:
            print("No tasks to edit")

        else:
            for i , task in enumerate(tasks):
                print(f"{i+1}. {task}")    

        try:
            num = int (input("Enter Task number for edit: "))

            if  0 < num <= len(tasks):
                newtask = input("Enter new task: ")
                
                if newtask == "":
                    print("task cannot be empty: ")

                else:#

                    clean_tasks = [t.split("(") [0] for t in tasks]

                    if newtask in clean_tasks:
                      print("Task already exists! ")

                    else:
                        tasks[num - 1] = f"{newtask} (edited: {datetime.now().strftime('%Y-%m-%d')})"
                        save_tasks()
                        print("Task edited successfully!")
  

            else:
                print("Invalid number")    

        except ValueError:
            print("Invalid input")          

    # Exit
    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")
        input("\nPress Enter...")

print(FILE_PATH)        