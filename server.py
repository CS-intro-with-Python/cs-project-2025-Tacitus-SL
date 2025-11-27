from flask import Flask, render_template, request, redirect, url_for, abort
from datetime import datetime

app = Flask(__name__)

tasks = []
next_id = 1


class Task:
    def __init__(self, id, subject, description, due_date, status="in progress"):
        self.id = id
        self.subject = subject
        self.description = description
        self.due_date = due_date
        self.status = status


def find_task(task_id):
    for task in tasks:
        if task.id == task_id:
            return task
    return None


@app.route("/")
def home():
    status = request.args.get("status", "all")
    sort = request.args.get("sort", "none")

    filtered = tasks.copy()

    if status == "in-progress":
        filtered = [t for t in tasks if t.status == "in progress"]
    elif status == "completed":
        filtered = [t for t in tasks if t.status == "completed"]
    if sort == "date":
        filtered.sort(key=lambda t: t.due_date)
    elif sort == "subject":
        filtered.sort(key=lambda t: t.subject.lower())
    elif sort == "status":
        order = {"in progress": 0, "completed": 1}
        filtered.sort(key=lambda t: order.get(t.status, 99))

    return render_template("index.html", tasks=filtered, status=status, sort=sort)

@app.route("/task/add", methods=["GET", "POST"])
def add_task():
    global next_id

    if request.method == "POST":
        t = Task(
            id=next_id,
            subject=request.form["subject"],
            description=request.form["description"],
            due_date=request.form["due_date"],
        )
        tasks.append(t)
        next_id += 1
        return redirect(url_for("home"))

    return render_template("add_task.html")


@app.route("/task/<int:task_id>/edit", methods=["GET", "POST"])
def edit_task(task_id):
    task = find_task(task_id)
    if not task:
        abort(404)

    if request.method == "POST":
        task.subject = request.form["subject"]
        task.description = request.form["description"]
        task.due_date = request.form["due_date"]
        task.status = request.form["status"]
        return redirect(url_for("home"))

    return render_template("edit_task.html", task=task)


@app.route("/task/<int:task_id>/delete", methods=["GET", "POST"])
def delete_task(task_id):
    task = find_task(task_id)
    if not task:
        abort(404)

    if request.method == "POST":
        tasks.remove(task)
        return redirect(url_for("home"))

    return render_template("delete_task.html", task=task)


@app.route("/task/<int:task_id>/complete", methods=["GET", "POST"])
def complete_task(task_id):
    task = find_task(task_id)
    if not task:
        abort(404)

    if request.method == "POST":
        task.status = "completed"
        return redirect(url_for("home"))

    return render_template("complete_task.html", task=task)

@app.template_filter('format_date')
def format_date(value):
    if not value:
        return ""
    return datetime.strptime(value, "%Y-%m-%d").strftime("%d/%m/%Y")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
