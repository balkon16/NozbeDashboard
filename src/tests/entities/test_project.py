from decimal import Decimal

import pytest
from datetime import datetime, timedelta

from src.modules.entities.project import Project
from src.modules.entities.task import Task


def test_valid_project_creation():
    """Test that a project can be created with valid dates."""
    now = datetime.now()
    project = Project(id="1", name="Test project", created_at=now, last_updated_at=now, is_completed=False)
    assert project.id == "1"
    assert project.name == "Test project"
    assert project.created_at == now
    assert project.last_updated_at == now
    assert project.is_completed is False


def test_last_updated_at_equal_to_created_at():
    """Test that a project can be created when last_updated_at is equal to created_at."""
    now = datetime.now()
    project = Project(id="1", name="Test project", created_at=now, last_updated_at=now, is_completed=False)
    assert project.created_at == project.last_updated_at


def test_last_updated_at_later_than_created_at():
    """Test that a project can be created when last_updated_at is later than created_at."""
    created_at = datetime.now()
    last_updated_at = created_at + timedelta(days=1)
    project = Project(id="1", name="Test project", created_at=created_at, last_updated_at=last_updated_at,
                      is_completed=False)
    assert project.last_updated_at > project.created_at


def test_invalid_project_creation():
    """Test that a ValueError is raised when last_updated_at is earlier than created_at."""
    created_at = datetime.now()
    last_updated_at = created_at - timedelta(days=1)
    with pytest.raises(ValueError) as excinfo:
        Project(id="1", name="Test project", created_at=created_at, last_updated_at=last_updated_at, is_completed=False)
    assert "last_updated_at cannot be earlier than created_at." in str(excinfo.value)


def test_add_multiple_tasks_to_project():
    """Test adding multiple tasks to a project."""
    now = datetime.now()

    # Create a project
    project = Project(
        id="project1",
        name="Test Project",
        created_at=now,
        last_updated_at=now,
        is_completed=False,
    )

    # Create two tasks associated with the project
    task1 = Task(
        id="task1",
        name="Task 1",
        time=Decimal("5.0"),
        is_completed=False,
        last_updated_at=now,
    )
    task2 = Task(
        id="task2",
        name="Task 2",
        time=Decimal("3.0"),
        is_completed=True,
        last_updated_at=now,
    )

    # Add the tasks to the project
    project.add_task(task1)
    project.add_task(task2)

    # Assert that the tasks are in the project's task list
    assert len(project.tasks) == 2
    assert task1 in project.tasks
    assert task2 in project.tasks

