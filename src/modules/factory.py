import logging
from datetime import datetime, timezone
from decimal import Decimal
from typing import List, Dict

from .entities.project import Project
from .entities.task import Task


class EntityFactory:
    """
    A factory class for creating Task and Project objects from API data.
    """

    @staticmethod
    def create_task(task_data: Dict) -> Task:
        """
        Creates a Task object from a dictionary of task data.
        """
        try:
            duration_minutes = int(task_data["time"])
        except KeyError:
            raise ValueError("Task data must contain 'time' key.")

        try:
            ts = float(task_data["ts"])
        except KeyError:
            raise ValueError("Task data must contain 'ts' key.")
        except ValueError:
            raise ValueError(f"Can't translate {task_data['ts']} to a float.")

        return Task(
            id=task_data["id"],
            name=task_data["name"],
            duration=Decimal(duration_minutes / 60),  # Convert minutes to hours
            is_completed=task_data["completed"],
            last_updated_at=datetime.fromtimestamp(ts, tz=timezone.utc),
            project_id=task_data["project_id"],  # Assuming project_id is present
        )

    @staticmethod
    def create_project(project_data: Dict, tasks: List[Task] = None) -> Project:
        """
        Creates a Project object from a dictionary of project data.
        Optionally accepts a list of tasks to associate with the project.
        """
        try:
            ts = project_data["ts"]
        except KeyError:
            raise ValueError("Project data must contain 'ts' key.")

        # TODO (low): it actually should be the Project responsible for creating
        #  fields (e.g. translating last_updated_at from string to datetime)
        constructor_data = {
            "id": project_data["id"],
            "name": project_data["name"],
            "last_updated_at": datetime.fromtimestamp(float(ts), tz=timezone.utc),
            "is_completed": project_data["_has_completed"]
        }
        created_at_str = project_data.get("_created_at")
        if created_at_str:
            constructor_data["created_at"] \
                = datetime.strptime(created_at_str, "%Y-%m-%d %H:%M:%S").replace(tzinfo=timezone.utc)
        else:
            logging.warning(f"{project_data['name']}: Missing value for 'created_at' field.")

        project = Project(**constructor_data)

        if tasks:
            project.tasks = tasks  # Assign tasks directly

        return project

    @staticmethod
    def create_tasks_from_list(tasks_data: List[Dict]) -> List[Task]:
        """
        Creates a list of Task objects from a list of task data dictionaries.
        """
        tasks = []
        for task_data in tasks_data:
            tasks.append(EntityFactory.create_task(task_data))
        return tasks

    @staticmethod
    def create_projects_from_list(projects_data: List[Dict], all_tasks: List[Dict] = None) -> List[Project]:
        """
        Creates a list of Project objects from a list of project data dictionaries.
        Optionally accepts a list of all tasks to associate with the projects.
        """
        projects = []
        for project_data in projects_data:
            # Filter tasks for the current project
            project_tasks = []
            if all_tasks:
                project_tasks_data = [task_data for task_data in all_tasks if
                                      task_data["project_id"] == project_data["id"]]
                project_tasks = EntityFactory.create_tasks_from_list(project_tasks_data)

            projects.append(EntityFactory.create_project(project_data, project_tasks))
        return projects
