todos = []

def create_task():
    task_name = input("Enter the task name :")
    todos.append({
        "id": len(todos),
        "Task name": task_name,
        "is_completed" : False
    })

    print("Task added Successfully")

def delete_task():
    task_id = input("Entre Task id") ,
    for idx, todo in enumerate(todos):
        if todo["id"] == task_id:
           todos.pop(idx)
        break
    print("Task Delete Successfully")

def mark_as_completed():
    task_id = input("Entre Task id")   
    for todo in todos:
        if todo["id"]== task_id:
            todo['is_completed']= True
            print("Task Completed")
            break
def view_task():
    print(todos)        



print("_______________________welcome to task Manager________________________") 
print("_____________________1.Create Task")   