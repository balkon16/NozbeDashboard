import datetime

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
