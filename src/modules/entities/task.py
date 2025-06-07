from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal


@dataclass
class Task:
    """
    Represents a task within a project.
    """

    id: str
    name: str
    duration: Decimal
    # TODO: can this be inferred from raw data?
    # is_completed: bool
    last_updated_at: datetime
    project_id: str  # TODO: do I need a reference to a Project object?

    def __post_init__(self):
        """
        Validates that time is non-negative.
        """
        if self.duration < 0:
            raise ValueError("Time must be a non-negative value.")
