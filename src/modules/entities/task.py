from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.modules.entities.project import Project  # Avoid circular import


@dataclass
class Task:
    """
    Represents a task within a project.
    """

    id: str
    name: str
    time: Decimal
    is_completed: bool
    last_updated_at: datetime
    # project: Project # TODO: do I need a reference to a Project?

    def __post_init__(self):
        """
        Validates that time is non-negative.
        """
        if self.time < 0:
            raise ValueError("Time must be a non-negative value.")
