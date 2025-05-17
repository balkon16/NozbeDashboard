import csv
import logging
from typing import List
from dataclasses import asdict

from .base_saver import DataSaver
from .dtos import TaskOutputDTO
from ..entities.project import Project


class CsvSaver(DataSaver):
    """
    Saves data to a CSV file.
    """

    def save(self, projects: List[Project], filepath: str, **kwargs) -> None:
        """
        Saves project tasks data to a CSV file.

        Args:
            projects: A list of Project objects.
            filepath: The path to the output CSV file.
        """
        if not filepath.lower().endswith(".csv"):
            filepath += ".csv"

        prepared_dtos: List[TaskOutputDTO] = self._prepare_data_for_saving(projects)

        if not prepared_dtos:
            logging.warning(f"No data to save to {filepath}.")
            return

        data_to_save = [asdict(dto) for dto in prepared_dtos]
        headers = list(TaskOutputDTO.__annotations__.keys())

        try:
            with open(filepath, "w", newline="", encoding="utf-8") as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=headers)
                writer.writeheader()
                for row_dict in data_to_save:
                    writer.writerow(row_dict)
            logging.info(f"Data successfully saved to {filepath}")
        except IOError as e:
            logging.error(f"Error saving data to {filepath}: {e}")
        except Exception as e:
            logging.error(f"An unexpected error occurred during CSV saving: {e}")
