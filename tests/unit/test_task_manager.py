"""
Module:
    test_task_manager.py

Purpose:
    Unit tests for the TaskManager class.

Coverage:
    - Add tasks
    - Retrieve tasks
    - Complete tasks
    - Undo tasks
    - Delete tasks

Author:
    Julio Soto
"""

from models.task import Task


class TestTaskManager:
    """Unit tests for the TaskManager class."""

    def test_add_task(self, task_manager, sample_task):
        """
        Verify that a task can be added successfully.
        """

        task_manager.add_task(sample_task)

        assert len(task_manager.get_all_tasks()) == 1
        assert task_manager.get_all_tasks()[0] == sample_task

    def test_get_all_tasks(self, task_manager):
        """
        Verify that all stored tasks are returned.
        """

        task_1 = Task("Task 1", "Description 1")
        task_2 = Task("Task 2", "Description 2")

        task_manager.add_task(task_1)
        task_manager.add_task(task_2)

        tasks = task_manager.get_all_tasks()

        assert len(tasks) == 2
        assert task_1 in tasks
        assert task_2 in tasks

    def test_get_task_by_id(self, task_manager, sample_task):
        """
        Verify that an existing task can be retrieved by ID.
        """

        task_manager.add_task(sample_task)

        task = task_manager.get_task_by_id(sample_task.id)

        assert task == sample_task

    def test_get_task_by_invalid_id(self, task_manager):
        """
        Verify that searching for a nonexistent task returns None.
        """

        task = task_manager.get_task_by_id("invalid-id")

        assert task is None

    def test_complete_task(self, task_manager, sample_task):
        """
        Verify that a task can be marked as completed.
        """

        task_manager.add_task(sample_task)

        result = task_manager.complete_task(sample_task.id)

        assert result is True
        assert sample_task.completed is True

    def test_undo_task(self, task_manager, sample_task):
        """
        Verify that a completed task can be restored.
        """

        task_manager.add_task(sample_task)

        task_manager.complete_task(sample_task.id)

        result = task_manager.undo_task(sample_task.id)

        assert result is True
        assert sample_task.completed is False

    def delete_existing_task(self, task_manager, sample_task):
        """
        Verify that an existing task can be deleted.
        """

        task_manager.add_task(sample_task)

        result = task_manager.delete_task(sample_task.id)

        assert result is True
        assert len(task_manager.get_all_task()) == 0

    def test_delete_nonexistent_task(self, task_manager):
        """
        Verify that deleting a nonexistent task returns False.
        """

        result = task_manager.delete_task("invalid-id")

        assert result is False
