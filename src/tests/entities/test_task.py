import pytest
from datetime import datetime
from decimal import Decimal

from src.modules.entities.task import Task


# TODO: support recurring tasks
def test_task_creation():
    """Test successful Task creation."""
    now = datetime.now()
    task = Task(
        id="task1",
        name="Test Task",
        duration=Decimal("10.5"),
        is_completed=False,
        last_updated_at=now,
        project_id="ID-123",
    )
    assert task.id == "task1"
    assert task.name == "Test Task"
    assert task.duration == Decimal("10.5")
    assert task.is_completed is False
    assert task.last_updated_at == now
    assert task.project_id == "ID-123"


def test_task_creation_with_zero_time():
    """Test successful Task creation with zero time."""
    now = datetime.now()
    task = Task(
        id="task1",
        name="Test Task",
        duration=Decimal("0"),
        is_completed=False,
        last_updated_at=now,
        project_id="ID-123",
    )
    assert task.duration == Decimal("0")


def test_task_creation_negative_time():
    """Test Task creation with negative time raises ValueError."""
    now = datetime.now()
    with pytest.raises(ValueError) as excinfo:
        Task(
            id="task1",
            name="Test Task",
            duration=Decimal("-1"),
            is_completed=False,
            last_updated_at=now,
            project_id="ID-123",
        )
    assert "Time must be a non-negative value." in str(excinfo.value)
