from . import app, db
from flask import redirect, url_for, request, render_template
from .models import Task
from .forms import TaskForm

@app.route("/")
def home():
    #incomplete = db.query.filter_by(completed=False).all()
    #complete = db.query.filter_by(completed=True).all()
    
    tasks = Task.query.all()

    result = ""
    for task in tasks:
        result += "{0.id:0>3} | {0.description} | {completed}<br>".format(task, completed="✅" if task.completed else "❌")

    return result

@app.route("/create", methods=["GET", "POST"])
def create():
    form = TaskForm()

    if request.method == "POST":
        new_task = Task(description=form.description.data)
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for("home"))
    else:
        return render_template("create.html", form=form)

@app.route("/update/<int:id>/<description>")
def update(id,description):
    task = Task.query.get(id)
    task.description = description
    db.session.add(task)
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/delete/<int:id>")
def delete(id):
    task = Task.query.get(id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/complete/<int:id>")
def complete(id):
    task = Task.query.get(id)
    task.completed = True
    db.session.add(task)
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/incomplete/<int:id>")
def incomplete(id):
    task = Task.query.get(id)
    task.completed = True
    db.session.add(task)
    db.session.commit()
    return redirect(url_for("home"))
