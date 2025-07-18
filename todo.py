import json

todo = "todo.json" 

def load_tasks():
    try: 
        with open(todo, "r") as file:
            return json.load(file)  
    except: 
        return {"tasks": []}

def add_tasks(tasks):
    description = input("Enter the task description: ").strip()
    if description:
        tasks["tasks"].append({"description": description, "complete": False})
        save_tasks(tasks)
        print("Task added")
    else:
        print("Description cannot be empty")


def save_tasks(tasks):
    try:
        with open(todo, "w") as file:
            json.dump(tasks, file)
    except: 
        print("Failed to save")
    

def view_tasks(tasks):
   task_list = tasks["tasks"]
   if len(task_list) == 0:
       print("There is no tasks.")
   else:
       print("Your To-Do List: ")

   for idx, task in enumerate(task_list):
       status = "[Complete]" if task["complete"] else ["Pending"]
       print(f"{idx + 1}. {task['description']} | {status}")


def mark_tasks_complete(tasks):
    view_tasks(tasks)
    try:
        task_number = int(input("Enter the task number to mark as complete: ").strip())
        if 1 <= task_number <= len(tasks):
            tasks["tasks"][task_number - 1]["complete"] = True 
            save_tasks(tasks)
            print("Task marked as complete.")   
        else:
            print("Invalid task number.")
    except:
        print("Enter a valid number.")
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
  

#add : Task as incompleted
#add : Delete task





