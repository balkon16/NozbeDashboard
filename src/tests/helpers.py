import json
from typing import List, Dict, Any


def get_json_mock_file(scenario_name: str, entity_name: str) -> Dict[str, Any] | List[Dict[str, Any]]:
    with open(f"src/tests/mocks/{scenario_name}/{entity_name}.json") as f:
        return json.load(f)
