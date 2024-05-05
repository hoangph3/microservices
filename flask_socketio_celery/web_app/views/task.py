from flask import Blueprint, render_template


task = Blueprint('task', __name__)


@task.route('/')
def index():
    return render_template("index.html")
