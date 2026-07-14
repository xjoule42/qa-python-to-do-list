from flask import Flask

from models.task_manager import TaskManager
from routes.web import create_web_blueprint
from services.storage import Storage


app = Flask(__name__)

# Initialize services
storage = Storage("data/tasks.json")

# Initialize task manager
task_manager = TaskManager()

# Load existing tasks
loaded_tasks = storage.load_tasks()

for task in loaded_tasks:
    task_manager.add_task(task)

# Register application routes
app.register_blueprint(
    create_web_blueprint(task_manager)
)


if __name__ == "__main__":
    app.run(debug=True)