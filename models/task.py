import uuid
from datetime import datetime


class Task:
    """Represents a single task in the to-do list."""

    def __init__(self, title: str, description: str = ""):
        self.id = str(uuid.uuid4())
        self.title = title
        self.description = description
        self.completed = False
        self.created_at = datetime.now().isoformat()

    def complete(self) -> None:
        """Mark the task as completed."""
        self.completed = True

    def undo(self) -> None:
        """Mark the task as pending."""
        self.completed = False

    def to_dict(self) -> dict:
        """Convert the task into a dictionary."""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed,
            "created_at": self.created_at,
        }

    def __str__(self) -> str:
        status = "✓" if self.completed else "✗"
        return (
            f"[{status}] {self.title} "
            f"(Created: {self.created_at})"
        )