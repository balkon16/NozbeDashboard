import logging
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import List, Optional

from .task import Task


@dataclass
class Project:
    """
    Represents a project with its attributes.
    """

    id: str
    name: str
    last_updated_at: datetime
    # TODO: verify if this can be inferred from data
    # is_completed: bool
    created_at: Optional[datetime] = datetime(1970, 1, 1, tzinfo=timezone.utc)
    tasks: List[Task] = field(default_factory=list)

    def __post_init__(self):
        """
        Validates that last_updated_at is not earlier than created_at.
        """
        if self.last_updated_at <= self.created_at:
            # it used to be a ValueError("last_updated_at cannot be earlier than created_at.") but for some projects source data
            #  was faulty
            # TODO: conduct analysis and do something about it -> add appropriate changes to the tests (*1)
            logging.warning(f"{self.name}: last_updated_at is earlier than created_at.")

    def add_task(self, task: Task):
        """Adds a task to the project."""
        self.tasks.append(task)
