from dataclasses import dataclass
from decimal import Decimal


@dataclass
class TaskOutputDTO:
    """
    Data Transfer Object for task output.
    """
    name: str
    duration: Decimal
    is_completed: bool
    project_name: str