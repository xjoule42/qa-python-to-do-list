import pytest

from models.task import Task
from models.task_manager import TaskManager
from services.storage import Storage
from app import create_app

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

@pytest.fixture
def client():
    """
    Returns a Flask test client.
    """

    app = create_app()
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client
