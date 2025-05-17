import logging
from abc import ABC, abstractmethod
from typing import List, Dict


class DataProvider(ABC):
    """
    Abstract base class for data providers.  Defines the interface for
    fetching projects and tasks.  Also configures logging.
    """

    def __init__(self, log_level=logging.INFO):
        """
        Initializes the DataProvider and configures logging.

        Args:
            log_level: The logging level to use (e.g., logging.INFO, logging.DEBUG).
        """
        logging.basicConfig(level=log_level, format='%(asctime)s - %(levelname)s - %(message)s')
        self.logger = logging.getLogger(__name__)

    @abstractmethod
    def get_projects(self) -> List[Dict]:
        """
        Abstract method to fetch a list of projects.

        Returns:
            list: A list of dictionaries, where each dictionary represents a project.
        """
        raise NotImplementedError()

    @abstractmethod
    def get_tasks(self) -> List[Dict]:
        """
        Abstract method to fetch a list of tasks.

        Returns:
            list: A list of dictionaries, where each dictionary represents a task.
        """
        raise NotImplementedError()
