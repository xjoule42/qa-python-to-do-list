from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
)

from models.task import Task
from models.task_manager import TaskManager
from services.storage import Storage


def create_web_blueprint(
    task_manager: TaskManager,
    storage: Storage,
) -> Blueprint:

    web = Blueprint("web", __name__)

    @web.route("/")
    def home():
        """Display all tasks."""
        tasks = task_manager.get_all_tasks()

        return render_template(
            "index.html",
            tasks=tasks,
        )

    @web.route("/add", methods=["POST"])
    def add_task():
        """Create a new task."""

        title = request.form.get("title", "").strip()
        description = request.form.get("description", "").strip()

        if not title:
            return redirect(url_for("web.home"))

        task = Task(
            title=title,
            description=description,
        )

        task_manager.add_task(task)

        storage.save_tasks(
            task_manager.get_all_tasks()
        )

        return redirect(url_for("web.home"))

    return web