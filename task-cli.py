import sys
import json
from datetime import datetime
command = sys.argv[1]

# Read existing tasks
def loadTasks(t:list[dict]):
    try:
        with open("tasks.json", "r") as file:
            t = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        t = []
    return t

# Save everything back
def saveTasks(t:list[dict]):
    with open("tasks.json","w") as file:
        json.dump(t, file, indent = 4)

def add():
    tasks = []
    tasks = loadTasks(tasks)
    newTask = {
        "task_id" : len(tasks) + 1,
        "description"  : sys.argv[2],
        "status" : "todo",
        "createdAt" : datetime.now().isoformat()
    }
    tasks.append(newTask)
    saveTasks(tasks)

def update():
    id = int(sys.argv[2])
    newdesc = sys.argv[3]
    tasks = []
    tasks = loadTasks(tasks)
    for task in tasks:
        if task["task_id"] == id:
            task["description"] = newdesc
            task["updatedAt"] = datetime.now().isoformat()
            break
    saveTasks(tasks)

def delete():
    id = int(sys.argv[2])
    tasks = []
    tasks = loadTasks(tasks)
    try:
        for task in tasks:
            if task["task_id"] == id:
                del(task)
    except IndexError:
        print("Task not found.")
    saveTasks(tasks)

def markInProgress():
    tasks = []
    tasks = loadTasks(tasks)
    id = int(sys.argv[2])
    for task in tasks:
        if task["task_id"] == id:
            tasks[id]["status"] = "in progress"
            tasks[id]["updatedAt"] = datetime.now().isoformat()
    saveTasks(tasks)

def markDone():
    tasks = []
    tasks = loadTasks(tasks)
    id = int(sys.argv[2])
    for task in tasks:
        if task["task_id"] == id:
            tasks[id]["status"] = "done"
            tasks[id]["updatedAt"] = datetime.now().isoformat()
    saveTasks(tasks)

def listTasks():
    tasks = []
    tasks = loadTasks(tasks)
    for task in tasks:
        print(f'{task["task_id"]}. {task}')

def listDone():
    tasks = []
    tasks = loadTasks(tasks)
    for task in tasks:
        if task["status"] == "done":
            print(f'{task["task_id"]}. {task}')

def listToDo():
    tasks = []
    tasks = loadTasks(tasks)
    for task in tasks:
        if task["status"] == "todo":
            print(f'{task["task_id"]}. {task}')

def listInProg():
    tasks = []
    tasks = loadTasks(tasks)
    for task in tasks:
        if task["status"] == "in progress":
            print(f'{task["task_id"]}. {task}')

commands = {
    "add": add,
    "update": update,
    "delete": delete,
    "mark-in-progress": markInProgress,
    "mark-done" : markDone
}

if command in commands:
    commands[command]()

elif command == "list" :
    if len(sys.argv) == 2:
        listTasks()
    elif sys.argv[2] == "todo":
        listToDo()
    elif sys.argv[2] == "in-progress":
        listInProg()
    elif sys.argv[2] == "done":
        listDone()
    else:
        print("Invalid list option.")
else : 
    print("wrong choose!!\n" \
    "choose one of this operation!\n" \
    "add\nupdate\ndelete\nmark-in-progress\nmark-done\n" \
    "list\nlist done|| todo|| in-progress")