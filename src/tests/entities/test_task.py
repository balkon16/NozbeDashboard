import pytest
from datetime import datetime
from decimal import Decimal

from src.modules.entities.task import Task
# from src.modules.entities.project import Project

now = datetime.now()
# test_project = Project(id="1", name="Test project", created_at=now, last_updated_at=now, is_completed=False)

# TODO: support recurring tasks
def test_task_creation():
    """Test successful Task creation."""
    now = datetime.now()
    task = Task(
        id="task1",
        name="Test Task",
        time=Decimal("10.5"),
        is_completed=False,
        last_updated_at=now,
        # project=test_project,
    )
    assert task.id == "task1"
    assert task.name == "Test Task"
    assert task.time == Decimal("10.5")
    assert task.is_completed is False
    assert task.last_updated_at == now
    # assert isinstance(task.project, Project)


def test_task_creation_with_zero_time():
    """Test successful Task creation with zero time."""
    now = datetime.now()
    task = Task(
        id="task1",
        name="Test Task",
        time=Decimal("0"),
        is_completed=False,
        last_updated_at=now,
        # project=test_project,
    )
    assert task.time == Decimal("0")


def test_task_creation_negative_time():
    """Test Task creation with negative time raises ValueError."""
    now = datetime.now()
    with pytest.raises(ValueError) as excinfo:
        Task(
            id="task1",
            name="Test Task",
            time=Decimal("-1"),
            is_completed=False,
            last_updated_at=now,
            # project=test_project,
        )
    assert "Time must be a non-negative value." in str(excinfo.value)
