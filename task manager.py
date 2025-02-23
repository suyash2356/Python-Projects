import os

#File to store items
FILE_NAME="tasks.txt"

# Load tasks from file
def load_tasks():
    tasks = {}
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                parts = line.strip().split(" | ")
                if len(parts) == 4:  # Ensure correct number of values
                    task_id, Title, Status, Deadline = parts
                    tasks[int(task_id)] = {"Title": Title, "Status": Status, "Deadline": Deadline}
                else:
                    print(f"Skipping invalid line: {line.strip()}")  # Debugging output
    return tasks


# save tasks to file
def save_task(tasks):
    with open(FILE_NAME,"w") as file:
        for task_id, task in tasks.items():
            file.write(f"{task_id} | {task['Title']} | {task['Status']} | {task['Deadline']}\n")

# Add a new task
def add_task(tasks):
    Title=input("Enter task title:")
    task_id=max(tasks.keys(), default=0)+1
    ans=input("Do you want to set deadline for this task or not:")
    if ans=="yes":
        Deadline=input("Set a deadline for your task:")
    elif ans=="no":
        print("Deadline not set for this task.")
    else:
        print("Invalid Answer.")   
     
    tasks[task_id]={"Title":Title, "Status":"incomplete","Deadline":Deadline}
    print(f"Task '{Title}' added.")
    print(f"Deadline set to '{Deadline}'")
   
        
    
# view all tasks
def view_tasks(tasks):
    if not tasks:
        print("Task not available")   
    else:
        for task_id, task in tasks.items():
            print(f"[{task_id}] {task['Title']} - {task['Status']} - {task['Deadline']}")
       
# Mark task as complete
def mark_task_complete(tasks):
    task_id=int(input("Enter task ID to mark as complete:"))
    if task_id in tasks:
        tasks[task_id] ["Status"] = "Complete"
        print(f"Task '{tasks[task_id]['title']}' marked as complete.")
    else:
        print("Task ID not found.")
        
# Delete a task
def delete_task(tasks):
    task_id=int(input("Enter task ID to delete:"))
    if task_id in tasks:
        deleted_task = tasks.pop(task_id)
        print(f"Task '{deleted_task['title']}' deleted.")
    else:
        print("Task ID not found.")        
                        
# Main Menu
def main():
    tasks=load_tasks()                       
    while True:
        print("\nTask Manager Menu")
        print('Press 1 to add task')
        print('Press 2 to view task')
        print('Press 3 to mark task as complete')
        print('Press 4 to Delete task')
        print('Press 5 to exit')
        choice=int(input("Enter your choice:"))
        if choice==1:
            add_task(tasks)
        elif choice==2:
            view_tasks(tasks)    
        elif choice==3:
            mark_task_complete(tasks)
        elif choice==4:
            delete_task(tasks)
        elif choice==5:
            save_task(tasks) 
            break
        else:
            print("Invalid choice. Please try again")
            
if __name__=="__main__":
    main()                        