from dataclasses import dataclass, field
from datetime import datetime
from typing import List

from src.modules.entities.task import Task


@dataclass
class Project:
    """
    Represents a project with its attributes.
    """

    id: str
    name: str
    created_at: datetime
    last_updated_at: datetime
    is_completed: bool
    tasks: List[Task] = field(default_factory=list)

    def __post_init__(self):
        """
        Validates that last_updated_at is not earlier than created_at.
        """
        if self.last_updated_at < self.created_at:
            raise ValueError(
                "last_updated_at cannot be earlier than created_at."
            )

    def add_task(self, task: Task):
        """Adds a task to the project."""
        self.tasks.append(task)
