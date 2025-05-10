from typing import Any, Tuple, List, Dict

import pytest
from src.tests.helpers import get_json_mock_file


@pytest.fixture
def get_scenario01_raw_data() -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
    raw_projects = get_json_mock_file("scenario01", "projects")
    raw_tasks = get_json_mock_file("scenario01", "tasks")
    return raw_projects, raw_tasks
