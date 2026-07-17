from models.task import Task


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task: Task) -> None:
        """Add a new task to the task list."""
        self.tasks.append(task)

    def delete_task(self, task_id: str) -> bool:
        """Remove a task by its ID. Returns True if removed, False if not found."""
        for task in self.tasks:
            if task.id == task_id:
                self.tasks.remove(task)
                return True
        return False

    def get_all_tasks(self) -> list:
        """Return a list of all tasks."""
        return self.tasks.copy()

    def get_task_by_id(self, task_id: str) -> Task | None:
        """Retrieve a task by its ID. Returns None if not found."""
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def complete_task(self, task_id: str) -> bool:
        """
        Mark a task as completed by its ID.
        Returns True if successful, False if not found.
        """
        task = self.get_task_by_id(task_id)
        if task:
            task.complete()
            return True
        else:
            return False

    def undo_task(self, task_id: str) -> bool:
        """
        Mark a task as pending by its ID.
        Returns True if successful, False if not found.
        """
        task = self.get_task_by_id(task_id)
        if task:
            task.undo()
            return True
        else:
            return False
