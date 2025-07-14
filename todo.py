import json



def load_tasks():
    pass

def add_tasks():
    pass

def save_tasks():
    pass

def view_tasks():
    pass

def mark_tasks_complete():
    pass

def main():
    tasks = load_tasks()

    while True:
        
        print("\nTo-Do List Manager")
        
        print("\n1. View the tasks")
        print("2. Add a task")
        print("3. Complete Task")
        print("4. Exit")

        result = input("\nEnter your choice: ").strip()   

        if result == "1":
            view_tasks(tasks)
        elif result == "2":
            add_tasks(tasks)
        elif result == "3":
            mark_tasks_complete(tasks)
        elif result == "4":
            print("Ciao")
            break 
        else:
            print("Invalid Choice, please insert a number from 1 to 5")
        
main()
  

    





