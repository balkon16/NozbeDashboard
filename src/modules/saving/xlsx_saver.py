import logging
from typing import List

import pandas as pd

from dataclasses import asdict

from .base_saver import DataSaver
from .dtos import TaskOutputDTO
from ..entities.project import Project


# TODO: you can't add duration numbers in the generated file -> output_project_tasks_20250517_1523.xlsx
class XlsxSaver(DataSaver):
    """
    Saves data to an XLSX (Excel) file.
    """

    def save(self, projects: List[Project], filepath: str, **kwargs) -> None:
        """
        Saves project tasks data to an XLSX file.

        Args:
            projects: A list of Project objects.
            filepath: The path to the output XLSX file.
            **kwargs: Can include 'sheet_name'.
        """
        if not filepath.lower().endswith(".xlsx"):
            filepath += ".xlsx"

        sheet_name = kwargs.get("sheet_name", "TasksData")
        prepared_dtos: List[TaskOutputDTO] = self._prepare_data_for_saving(projects)

        if not prepared_dtos:
            logging.warning(f"No data to save to {filepath}.")
            return

        try:
            data_for_df = [asdict(dto) for dto in prepared_dtos]
            df = pd.DataFrame(data_for_df)
            df.to_excel(filepath, sheet_name=sheet_name, index=False, engine="openpyxl")
            logging.info(f"Data successfully saved to {filepath} (Sheet: {sheet_name})")
        except IOError as e:
            logging.error(f"Error saving data to {filepath}: {e}")
        except Exception as e:
            logging.error(f"An unexpected error occurred during XLSX saving: {e}")
