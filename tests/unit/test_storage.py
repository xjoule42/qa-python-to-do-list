"""
Module:
    test_storage.py

Purpose:
    Unit tests for the Storage service.

Coverage:
    - Save tasks
    - Load tasks
    - Empty storage
    - Missing file handling

Author:
    Julio Soto
"""

from models.task import Task


class TestStorage:
    """Unit tests for the Storage service."""

    def test_save_tasks(self, storage, sample_task):
        """
        Verify that tasks are saved successfully.
        """

        storage.save_tasks([sample_task])

        assert storage.storage_path.exists()

    def test_load_tasks(self, storage, sample_task):
        """
        Verify that saved tasks can be loaded.
        """

        storage.save_tasks([sample_task])

        tasks = storage.load_tasks()

        assert len(tasks) == 1
        assert tasks[0].title == sample_task.title
        assert tasks[0].description == sample_task.description

    def test_save_empty_task_list(self, storage):
        """
        Verify that an empty task list can be saved.
        """

        storage.save_tasks([])

        tasks = storage.load_tasks()

        assert tasks == []

    def test_load_missing_file_returns_empty_list(self, storage):
        """
        Verify that loading without an existing file
        returns an empty list.
        """

        tasks = storage.load_tasks()

        assert tasks == []