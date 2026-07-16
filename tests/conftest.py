import pytest

from models.task import Task
from models.task_manager import TaskManager
from services.storage import Storage

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

@pytest.fixture
def task_manager():
    return TaskManager()

@pytest.fixture
def storage(tmp_path):
    """
    Returns a Storage instance unsing a temporary directory.
    """

    return Storage(tmp_path / "tasks.json")