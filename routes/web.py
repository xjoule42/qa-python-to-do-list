from flask import Blueprint, render_template

from models.task_manager import TaskManager


def create_web_blueprint(task_manager: TaskManager) -> Blueprint:
    web = Blueprint("web", __name__)

    @web.route("/")
    def home():
        tasks = task_manager.get_all_tasks()
        return render_template(
            "index.html",
            tasks=tasks
        )

    return web