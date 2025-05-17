import json
import logging
from typing import List, Dict

from modules.data_providers.abstract_data_provider import DataProvider


class LocalStorageDataProvider(DataProvider):
    """
    A data provider that fetches project and task data from local JSON files.
    """

    def __init__(self, projects_file: str = "input/projects.json"
                 , tasks_file: str = "input/tasks.json"
                 , log_level=logging.INFO):
        """
        Initializes the LocalStorageDataProvider with the paths to the project and task JSON files.

        Args:
            projects_file (str): Path to the JSON file containing project data.
            tasks_file (str): Path to the JSON file containing task data.
        """
        super().__init__(log_level)
        self.projects_file = projects_file
        self.tasks_file = tasks_file

    def _load_data(self, file_path: str) -> List[Dict]:
        """
        Loads data from the specified JSON file.

        Args:
            file_path (str): Path to the JSON file.

        Returns:
            list: A list of dictionaries containing the data.
        """
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
            logging.info(f"Data loaded successfully from {file_path}")
            return data
        except FileNotFoundError:
            logging.error(f"File not found: {file_path}")
            raise FileNotFoundError(f"File not found: {file_path}")
        except json.JSONDecodeError:
            logging.error(f"Invalid JSON format in file: {file_path}")
            raise json.JSONDecodeError(f"Invalid JSON format in file: {file_path}", "", 0)

    def get_projects(self) -> List[Dict]:
        """
        Fetches a list of projects from the local JSON file.

        Returns:
            list: A list of dictionaries, where each dictionary represents a project.
        """
        return self._load_data(self.projects_file)

    def get_tasks(self) -> List[Dict]:
        """
        Fetches a list of tasks from the local JSON file.

        Returns:
            list: A list of dictionaries, where each dictionary represents a task.
        """
        return self._load_data(self.tasks_file)
