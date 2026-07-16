from flask import Flask

from models.task_manager import TaskManager
from routes.web import create_web_blueprint
from services.storage import Storage


def create_app():
    app = Flask(__name__)

    storage = Storage("data/tasks.json")
    task_manager = TaskManager()

    loaded_tasks = storage.load_tasks()

    for task in loaded_tasks:
        task_manager.add_task(task)

    app.register_blueprint(
        create_web_blueprint(task_manager, storage)
    )

    return app


app = create_app()


if __name__ == "__main__":
    app.run(debug=True)