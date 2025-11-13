import json

todos = []


def load_task():
    result = None
    try:
        with open("todos.json", "r") as f:
            result = json.load(f)
    except:
        result = []

    return result


def update_file():
    with open("todos.json", "w") as f:
        json.dump(todos, f)


def create_task():
    task_name = input("Enter the task name :")
    todos.append({"id": len(todos), "Task name": task_name, "is_completed": False})

    print("Task added Successfully")


def delete_task():
    task_id = (input("Entre Task id"),)
    for idx, todo in enumerate(todos):
        if todo["id"] == task_id:
            todos.pop(idx)
        break
    print("Task Delete Successfully")


def mark_as_completed():
    task_id = input("Entre Task id")
    for todo in todos:
        if todo["id"] == task_id:
            todo["is_completed"] = True
            print("Task Completed")
            break


def view_task():
    # print("ID", {todo['id']})
    print(todos)


print("_______________________welcome to task Manager________________________")
print("_____________________1.Create Task")
print("_____________________2. Delete Task")
print("_____________________3. Complete the task")
print("_____________________4. Task is complete")
print("_____________________5. exit")
print(
    "_____________________Entre the following value for perform the task:_____________________________"
)


todos = load_task()

while True:

    x = int(input("Entre the task you want to perform :"))
    if x == 1:
        print("create task")
        create_task()
        update_file()
    elif x == 2:
        print("Delete Task")
        delete_task()
        update_file()
    elif x == 3:
        print("Complete task")
        mark_as_completed()
        update_file()
    elif x == 4:
        print("View Task")
        view_task()
    elif x == 5:
        break

    else:
        print("You entre Wrong value")
