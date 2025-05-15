from typing import Any, Tuple, List, Dict

import pytest
from src.tests.helpers import get_json_mock_file

json_type = Dict[str, Any]


@pytest.fixture
def get_scenario01_raw_data() -> Tuple[List[json_type], List[json_type]]:
    raw_projects = get_json_mock_file("scenario01", "projects")
    raw_tasks = get_json_mock_file("scenario01", "tasks")
    return raw_projects, raw_tasks


@pytest.fixture
def get_scenario02_raw_data() -> Tuple[List[json_type], List[json_type]]:
    raw_projects = get_json_mock_file("scenario02", "projects")
    raw_tasks = get_json_mock_file("scenario02", "tasks")
    return raw_projects, raw_tasks


@pytest.fixture
def get_scenario03_raw_data() -> Tuple[List[json_type], List[json_type]]:
    raw_projects = get_json_mock_file("scenario03", "projects")
    raw_tasks = get_json_mock_file("scenario03", "tasks")
    return raw_projects, raw_tasks
