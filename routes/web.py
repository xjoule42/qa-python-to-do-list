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
    """Create and configure the application's web routes."""

    web = Blueprint("web", __name__)

    @web.route("/")
    def home():
        """Display all tasks."""

        tasks = task_manager.get_all_tasks()

        completed_tasks = sum(task.completed for task in tasks)

        return render_template(
            "index.html", tasks=tasks, completed_tasks=completed_tasks
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

        storage.save_tasks(task_manager.get_all_tasks())

        return redirect(url_for("web.home"))

    @web.route("/complete/<task_id>", methods=["POST"])
    def complete_task(task_id: str):
        """Toggle task completion."""

        task = task_manager.get_task_by_id(task_id)

        if task is None:
            return redirect(url_for("web.home"))

        if task.completed:
            task_manager.undo_task(task_id)
        else:
            task_manager.complete_task(task_id)

        storage.save_tasks(task_manager.get_all_tasks())

        return redirect(url_for("web.home"))

    @web.route("/delete/<task_id>", methods=["POST"])
    def delete_task(task_id: str):
        """Delete a task."""

        task_manager.delete_task(task_id)

        storage.save_tasks(task_manager.get_all_tasks())

        return redirect(url_for("web.home"))

    return web
