import sys
import json
from datetime import datetime
command = sys.argv[1]

def add():
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        tasks = []
    
    newTask = {
        "id" : len(tasks) + 1,
        "description"  : sys.argv[2],
        "status" : "todo",
        "createdAt" : datetime.now().isoformat()
    }
    tasks.append(newTask)

    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

def update():
    id = int(sys.argv[2])
    newdesc = sys.argv[3]

    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        tasks = []
        
    tasks[id]["description"] = newdesc
    tasks[id]["updatedAt"] = datetime.now().isoformat()

    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

def delete():
    id = int(sys.argv[2])

    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        tasks = []
    del(tasks[id])

    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

def markInProgress():
    with open("tasks.json", "r") as file:
        tasks = json.load(file)

    id = int(sys.argv[2])
    tasks[id]["status"] = "in progress"
    tasks[id]["updatedAt"] = datetime.now().isoformat()

    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)


def markDone():
    with open("tasks.json", "r") as file:
        tasks = json.load(file)

    id = int(sys.argv[2])
    tasks[id]["status"] = "Done"
    tasks[id]["updatedAt"] = datetime.now().isoformat()

    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

def listTasks():
    with open("tasks.json", "r") as file:
        tasks = json.load(file)

    for i in range(0,len(tasks)):
        print(tasks[i])

def listDone():
    with open("tasks.json", "r") as file:
        tasks = json.load(file)

    for i in range(0,len(tasks)):
        if tasks[i]["status"] == "Done":
            print(tasks[i])

def listToDo():
    with open("tasks.json", "r") as file:
        tasks = json.load(file)

    for i in range(0,len(tasks)):
        if tasks[i]["status"] == "todo":
            print(tasks[i])

def listInProg():
    with open("tasks.json", "r") as file:
        tasks = json.load(file)

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
    print("wrong choose!!\nchoose one of this operation!\nadd\nupdate\ndelete\nmark-in-progress\nmark-done\nlist\nlist done|| todo|| in-progress")


