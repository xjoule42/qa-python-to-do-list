import pytest

from models.task import Task
from models.task_manager import TaskManager

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