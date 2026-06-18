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
    loadTasks(tasks)
    newTask = {
        "id" : len(tasks) + 1,
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
    loadTasks(tasks)
    tasks[id]["description"] = newdesc
    tasks[id]["updatedAt"] = datetime.now().isoformat()
    saveTasks(tasks)

def delete():
    id = int(sys.argv[2])
    tasks = []
    loadTasks(tasks)
    del(tasks[id])
    saveTasks(tasks)

def markInProgress():
    tasks = []
    loadTasks(tasks)
    id = int(sys.argv[2])
    tasks[id]["status"] = "in progress"
    tasks[id]["updatedAt"] = datetime.now().isoformat()
    saveTasks(tasks)

def markDone():
    tasks = []
    loadTasks(tasks)
    id = int(sys.argv[2])
    tasks[id]["status"] = "Done"
    tasks[id]["updatedAt"] = datetime.now().isoformat()
    saveTasks(tasks)

def listTasks():
    tasks = []
    loadTasks(tasks)
    for i in range(0,len(tasks)):
        print(tasks[i])

def listDone():
    tasks = []
    loadTasks(tasks)
    for i in range(0,len(tasks)):
        if tasks[i]["status"] == "Done":
            print(tasks[i])

def listToDo():
    tasks = []
    loadTasks(tasks)
    for i in range(0,len(tasks)):
        if tasks[i]["status"] == "todo":
            print(tasks[i])

def listInProg():
    tasks = []
    loadTasks(tasks)
    for i in range(0,len(tasks)):
        if tasks[i]["status"] == "in progress":
            print(tasks[i])

if command == "add":
    add()
elif command == "update" :
    update()
elif command == "delete":
    delete()
elif command == "mark-in-progress" : 
    markInProgress()
elif command == "mark-done" : 
    markDone()
elif command == "list" :

    if sys.argv[2] == "all":
        listTasks()
    elif sys.argv[2] == "todo":
        listToDo()
    elif sys.argv[2] == "in-progress":
        listInProg()
    else:
        listDone()
else : 
    print("wrong choose!!\n" \
    "choose one of this operation!\n" \
    "add\nupdate\ndelete\nmark-in-progress\nmark-done\n" \
    "list\nlist done|| todo|| in-progress")