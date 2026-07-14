import json
from pathlib import Path

from models.task import Task


class Storage:
    """Handles reading and writing tasks to a JSON file."""

    def __init__(self, storage_path: str):
        self.storage_path = Path(storage_path)
        self.storage_path.parent.mkdir(parents=True, exist_ok=True)

    def save_tasks(self, tasks: list[Task]) -> None:
        """Save all tasks to the JSON file."""

        data = [task.to_dict() for task in tasks]

        with self.storage_path.open("w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

    def load_tasks(self) -> list[Task]:
        """Load all tasks from the JSON file."""

        if not self.storage_path.exists():
            return []

        with self.storage_path.open("r", encoding="utf-8") as file:
            data = json.load(file)

        return [Task.from_dict(task_data) for task_data in data]