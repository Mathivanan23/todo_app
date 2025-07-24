from flask import Flask, render_template, request, redirect
import json
import os

app = Flask(__name__)
FILE = 'todo.json'

def load_tasks():
    if os.path.exists(FILE):
        try:
            with open(FILE, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []  # fallback if file is empty or corrupted
    return []


def save_tasks(tasks):
    with open(FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

@app.route('/')
def index():
    tasks = load_tasks()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        task_text = request.form['task']
        tasks = load_tasks()
        tasks.append({"task": task_text, "done": False})
        save_tasks(tasks)
        return redirect('/')
    return render_template('add.html')

@app.route('/complete/<int:task_id>')
def complete_task(task_id):
    tasks = load_tasks()
    if 0 <= task_id < len(tasks):
        tasks[task_id]['done'] = True
    save_tasks(tasks)
    return redirect('/')

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    tasks = load_tasks()
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    save_tasks(tasks)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
