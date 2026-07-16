from models.task import Task

def test_create_task():
    """A new task should be initialized with default values."""

    task = Task(
        title ="Learn Pytest",
        description = "Write the first unit test",
    )

    assert task.title == "Learn Pytest"
    assert task.description == "Write the first unit test"

    assert task.completed is False
    
    assert task.id is not None
    assert isinstance(task.id, str)

    assert task.created_at is not None
