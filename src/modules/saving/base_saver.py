from abc import ABC, abstractmethod
from typing import List

from modules.entities.project import Project
from modules.saving.dtos import TaskOutputDTO


class DataSaver(ABC):
    """
    Abstract base class for data saving strategies.
    """

    def _prepare_data_for_saving(self, projects: List[Project]) -> List[TaskOutputDTO]:
        """
        Transforms the list of Project objects (with their tasks)
        into a list of TaskOutputDTO objects suitable for tabular output.
        """
        output_data: List[TaskOutputDTO] = []
        for project in projects:
            for task in project.tasks:
                output_data.append(
                    TaskOutputDTO(
                        name=task.name,
                        duration=task.duration,
                        is_completed=task.is_completed,
                        project_name=project.name,
                    )
                )
        return output_data

    @abstractmethod
    def save(self, projects: List[Project], filepath: str, **kwargs) -> None:
        """
        Saves the data from the list of projects to the specified filepath.

        Args:
            projects: A list of Project objects.
            filepath: The path to the output file.
            **kwargs: Additional arguments specific to the saver (e.g., sheet_name for Excel).
        """
        pass
