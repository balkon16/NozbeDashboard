import json
import logging
import sys

import requests

from src.modules.rest.client import NozbeAPIClient
from src.modules.factory import EntityFactory

if __name__ == '__main__':
    try:
        client = NozbeAPIClient()
        raw_projects = client.get_projects()
        logging.info(f"Fetched {len(raw_projects)} projects.")
        for project in raw_projects:
            logging.info(f"Project Name: {project['name']}")

        raw_tasks = client.get_tasks()
        logging.info(f"Fetched {len(raw_tasks)} tasks.")

    except (FileNotFoundError, json.JSONDecodeError, KeyError, requests.exceptions.RequestException) as e:
        logging.error(f"An error occurred during API interaction: {e}")
        sys.exit(1)

    # TODO: the "Flask Web Development" project is missing its creation datetime? Why?
    # projects = EntityFactory.create_projects_from_list(raw_projects, raw_tasks)
    # print(f"Created {len(projects)} projects from raw data.")
