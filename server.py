from flask import Flask, render_template, request, redirect, url_for, abort
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, date

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tasks.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class Task(db.Model):
    __tablename__ = "tasks"

    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(1000))
    due_date = db.Column(db.Date, nullable = False)
    status = db.Column(db.String(50), default = "in progress")

    def to_dict(self):
        return {
            "id": self.id,
            "subject": self.subject,
            "description": self.description,
            "due_date": self.due_date.strftime("%Y-%m-%d"),
            "status": self.status,
        }

with app.app_context():
    db.create_all()

@app.route("/")
def home():
    status = request.args.get("status", "all")
    sort = request.args.get("sort", "none")

    tasks = db.session.query(Task).all()
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

    today = date.today()
    for t in filtered:
        t.due_date_obj = t.due_date
        t.overdue = t.due_date_obj < today and t.status != "completed"
        t.is_due_today = t.due_date_obj == today and t.status != "completed"

    return render_template("index.html", tasks=filtered, status=status, sort=sort)

@app.route("/task/add", methods=["GET", "POST"])
def add_task():
    if request.method == "POST":
        subject = request.form.get("subject", "").strip()
        description = request.form.get("description", "")
        due_date_str = request.form.get("due_date", "")

        error = None
        due_date_obj = None

        if not subject:
            error = "Subject is required."
        else:
            try:
                due_date_obj = datetime.strptime(due_date_str, "%Y-%m-%d").date()

                if due_date_obj.year < 2025:
                    error = "Date must be starting from 2025"
            except ValueError:
                error = "Invalid date format."

        if error:
            return render_template(
                "add_task.html",
                error=error,
                subject=subject,
                description=description,
                due_date=due_date_str
            )

        task = Task(
            subject=subject,
            description=description,
            due_date=due_date_obj,
        )
        db.session.add(task)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("add_task.html")


@app.route("/task/<int:task_id>/edit", methods=["GET", "POST"])
def edit_task(task_id):
    task = db.session.get(Task, task_id)
    if not task:
        abort(404)

    subject = task.subject
    description = task.description
    due_date_str = task.due_date.strftime("%Y-%m-%d")
    status = task.status
    error = None

    if request.method == "POST":
        subject = request.form.get("subject", "").strip()
        description = request.form.get("description", "")
        due_date_str = request.form.get("due_date", "")
        status = request.form.get("status")

        due_date_obj = None
        if not subject:
            error = "Subject is required"
        else:
            try:
                due_date_obj = datetime.strptime(due_date_str, "%Y-%m-%d").date()
                if due_date_obj.year < 2025:
                    error = "Date must be starting from 2025"
            except ValueError:
                error = "Invalid date format"

        if not error:
            task.subject = subject
            task.description = description
            task.due_date = due_date_obj
            task.status = status
            db.session.commit()
            return redirect(url_for("home"))

    return render_template("edit_task.html", task=task, error=error, subject=subject, description=description, due_date=due_date_str, status=status)


@app.route("/task/<int:task_id>/delete", methods=["GET", "POST"])
def delete_task(task_id):
    task = db.session.get(Task, task_id)
    if not task:
        abort(404)

    if request.method == "POST":
        db.session.delete(task)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("delete_task.html", task=task)


@app.route("/task/<int:task_id>/complete", methods=["GET", "POST"])
def complete_task(task_id):
    task = db.session.get(Task, task_id)
    if not task:
        abort(404)

    if request.method == "POST":
        task.status = "completed"
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("complete_task.html", task=task)

@app.template_filter('format_date')
def format_date(value):
    if not value:
        return ""
    return value.strftime("%d/%m/%Y")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
