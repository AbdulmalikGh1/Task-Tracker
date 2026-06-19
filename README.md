# Task Tracker CLI

A simple command-line task tracker built with Python. It allows you to create, update, delete, and manage your tasks using a JSON file for storage.

the project URL: https://roadmap.sh/projects/task-tracker
## Features

- Add a task
- Update a task
- Delete a task
- Mark a task as in progress
- Mark a task as done
- List all tasks
- List tasks by status

## Requirements

- Python 3.8 or later

## How to Run

Clone the repository:

```bash
git clone <repository-url>
cd <repository-folder>
```

Run the application using:

```bash
python main.py <command>
```

or

```bash
python3 main.py <command>
```

## Commands

### Add a task

```bash
python main.py add "Buy groceries"
```

### Update a task

```bash
python main.py update 1 "Buy groceries and milk"
```

### Delete a task

```bash
python main.py delete 1
```

### Mark a task as in progress

```bash
python main.py mark-in-progress 1
```

### Mark a task as done

```bash
python main.py mark-done 1
```

### List all tasks

```bash
python main.py list
```

### List completed tasks

```bash
python main.py list done
```

### List tasks in progress

```bash
python main.py list in-progress
```

### List todo tasks

```bash
python main.py list todo
```

## Data Storage

Tasks are stored in a local `tasks.json` file. The file is created automatically when the application runs for the first time.
