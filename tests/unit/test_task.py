"""
Module:
    test_task.py

Purpose:
    Unit tests for the Task model.

Coverage:
    - Task Creation
    - Complete Task
    - Undo Task
    - Dictionary serialization
    - Object Deserialization
    - String Representation

Author:
    Julio Soto
"""

import pytest
from models.task import Task
from datetime import datetime

# ========================================================================
# FIXTURES
# ========================================================================

@pytest.fixture
def sample_task():
    """
    Returns a default task instance.

    This fixture is reused accross multiple tests to avoid
    duplicating object creation.    
    """
    return Task(
        title="Learn Pytest",
        description = "Write unit tests"
    )

# ========================================================================
# TESTS
# ========================================================================

class TestTask:
    """Unit tests for the Task model."""

    def test_create_task(self, sample_task):
        """
        Verify that a task is initialized with the expected
        default values.
        """

        assert sample_task.title == "Learn Pytest"
        assert sample_task.description == "Write unit tests"

        assert sample_task.completed is False

        assert sample_task.id is not None
        assert isinstance(sample_task.id, str)

        assert sample_task.created_at is not None

    def test_complete_task(self, sample_task):
        """
        Verify that complete() marks a task as completed.
        """

        sample_task.complete()

        assert sample_task.completed is True

    def test_undo_task(self, sample_task):
        """
        Verify that undo() restores a completed task.
        """

        sample_task.complete()
        sample_task.undo()

        assert sample_task.completed is False

    def test_to_dict(self, sample_task):
        """
        Verify that a Task instance is correctly serialized
        into a dictionary.
        """

        task_dict = sample_task.to_dict()

        assert isinstance(task_dict, dict)

        assert task_dict["title"] == sample_task.title
        assert task_dict["description"] == sample_task.description
        assert task_dict["completed"] == sample_task.completed
        assert task_dict["id"] == sample_task.id
        assert task_dict["created_at"] == sample_task.created_at

    def test_from_dict(self):
        """
        Verify that a Task instance can be reconstructed
        from a dictionary.
        """

        data = {
            "id": "123",
            "title": "Learn Flask",
            "description": "Study Blueprints",
            "completed": True,
            "created_at": "2026-07-15T12:00:00"
        }

        task = Task.from_dict(data)

        assert task.id == data["id"]
        assert task.title == data["title"]
        assert task.description == data["description"]
        assert task.completed == data["completed"]
        assert task.created_at == data["created_at"]

    def test_string_representation(self, sample_task):
        """
        Verify the string representation of a task.
        """

        expected = (
            f"[✗] {sample_task.title} "
            f"(Created: {sample_task.created_at})"
        )

        assert str(sample_task) == expected
    
    def test_tasks_generate_unique_ids(self):
        """
        Verify that each Task instance generates
        a unique identifier.
        """

        task_1 = Task(
            title ="Task One",
            description="First Task"
        )

        task_2 = Task(
            title = "Task Two",
            description = "Second Task"
        )

        assert task_1.id != task_2.id
    
    def test_created_at_is_valid_iso_format(self, sample_task):
        """Verify that created_at is automatically generated
        and stored using a valid ISO 8601 datetime format.
        """
        assert sample_task.created_at is not None
        assert sample_task.created_at != ""