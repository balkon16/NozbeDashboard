from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal


@dataclass
class Task:
    """
    Represents a task within a project.
    """

    # TODO: add:
    #  > created_at and ended_at -> compute cycle time
    id: str
    name: str
    # TODO: must be based on either time_spent or time_needed (the former is post-factum, the latter ante-factum)
    duration: Decimal
    is_completed: bool
    last_updated_at: datetime
    project_id: str  # TODO: do I need a reference to a Project object?

    def __post_init__(self):
        """
        Validates that time is non-negative.
        """
        if self.duration < 0:
            raise ValueError("Time must be a non-negative value.")
