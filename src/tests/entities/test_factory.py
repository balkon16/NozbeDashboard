import datetime
from decimal import Decimal
from typing import List

from src.modules.entities.task import Task
from src.modules.factory import EntityFactory
from src.modules.entities.project import Project


def test_populate_empty_project(get_scenario01_raw_data):
    projects_raw, tasks_raw = get_scenario01_raw_data
    project_raw = projects_raw[0]
    assert Project(
        id="p6drAQ3diWQQ9YgG",
        name="Inbox",
        created_at=datetime.datetime(2019, 11, 30, 14, 0, 54, tzinfo=datetime.timezone.utc),
        last_updated_at=datetime.datetime(2025, 5, 10, 10, 43, 47, 553539, tzinfo=datetime.timezone.utc),
        is_completed=True

    ) == EntityFactory.create_project(project_raw, None)


def test_populate_project_with_tasks(get_scenario02_raw_data):
    projects_raw, tasks_raw = get_scenario02_raw_data
    # project_raw = projects_raw[0]
    projects: List[Project] = EntityFactory.create_projects_from_list(projects_raw, tasks_raw)
    assert (len(projects) == 1
            and len(projects[0].tasks) == 2)


def test_create_task(get_scenario02_raw_data):
    _, tasks_raw = get_scenario02_raw_data
    task_raw = tasks_raw[0]
    assert EntityFactory.create_task(task_raw) == Task(
        id="MF6vG1VaLi3EzeyS",
        name="The Last of Us - sezon 2",
        duration=Decimal("0"),
        is_completed=False,
        last_updated_at=datetime.datetime(2025, 4, 13, 13, 43, 15, 306786, tzinfo=datetime.timezone.utc),
        project_id="p6drAQ3diWQQ9YgG"
    )


def test_populate_multiple_projects(get_scenario03_raw_data):
    projects_raw, tasks_raw = get_scenario03_raw_data
    projects: List[Project] = EntityFactory.create_projects_from_list(projects_raw, tasks_raw)
    assert (len(projects) == 2
            and projects[0].name == "Inbox"
            and projects[1].name == "Nozbe - Test Project"
            and len(projects[0].tasks) == 1
            and len(projects[1].tasks) == 2
            and projects[1].tasks[0].name == 'Task no. 2 - recurring task'
            and projects[1].tasks[0].project_id == 'xyTlhIPTsqKoFUSQ'
            )
