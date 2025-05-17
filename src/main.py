import argparse
import json
import logging
import sys

import requests

from modules.data_providers.rest_api_data_provider import RestAPIDataProvider
from modules.data_providers.local_storage_data_provider import LocalStorageDataProvider
from modules.factory import EntityFactory
from modules.saving.base_saver import DataSaver
from modules.saving.csv_saver import CsvSaver
from modules.saving.xlsx_saver import XlsxSaver


def main():
    parser = argparse.ArgumentParser(description="Fetch and process project and task data.")
    parser.add_argument(
        "--data-provider",
        choices=["api", "local"],
        default="api",
        help="Specify the data provider to use: 'api' for Rest API, 'local' for Local Storage. Defaults to 'api'.",
    )
    parser.add_argument(
        "--projects-file",
        type=str,
        default="input/projects.json",
        help="Path to the projects JSON file (used with --data-provider local).",
    )
    parser.add_argument(
        "--tasks-file",
        type=str,
        default="input/tasks.json",
        help="Path to the tasks JSON file (used with --data-provider local).",
    )
    parser.add_argument(
        "--token-file",
        type=str,
        default="src/credentials/token.json",
        help="Path to the token JSON file (used with --data-provider api).",
    )
    parser.add_argument(
        "--log-level",
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        default="INFO",
        help="Set the logging level. Defaults to INFO.",
    )

    args = parser.parse_args()

    logging.basicConfig(level=getattr(logging, args.log_level), format='%(asctime)s - %(levelname)s - %(message)s')

    try:
        if args.data_provider == "api":
            client = RestAPIDataProvider(token_file=args.token_file, log_level=getattr(logging, args.log_level))
        elif args.data_provider == "local":
            client = LocalStorageDataProvider(projects_file=args.projects_file, tasks_file=args.tasks_file,
                                              log_level=getattr(logging, args.log_level))
        else:
            logging.error("Invalid data provider specified.")
            sys.exit(1)

        raw_projects = client.get_projects()
        logging.info(f"Fetched {len(raw_projects)} projects.")
        for project in raw_projects:
            logging.info(f"Project Name: {project['name']}")

        raw_tasks = client.get_tasks()
        logging.info(f"Fetched {len(raw_tasks)} tasks.")

    except (FileNotFoundError, json.JSONDecodeError, KeyError, requests.exceptions.RequestException) as e:
        logging.error(f"An error occurred: {e}")
        sys.exit(1)

    projects = EntityFactory.create_projects_from_list(raw_projects, raw_tasks)
    # TODO: completed tasks are missing, e.g. the "Architecture Patterns with Python"
    #  shows only two tasks (5 min & 0 min)
    #  one completed (45 min) is not present!
    logging.info(f"Created {len(projects)} projects from raw data.")

    csv_output_filepath = "output/project_tasks.csv"
    xlsx_output_filepath = "output/output_project_tasks.xlsx"

    csv_saver: DataSaver = CsvSaver()
    logging.info(f"Saving tasks to CSV: {csv_output_filepath}")
    csv_saver.save(projects, csv_output_filepath)

    xlsx_saver: DataSaver = XlsxSaver()
    logging.info(f"Saving tasks to XLSX: {xlsx_output_filepath}")
    xlsx_saver.save(projects, xlsx_output_filepath, sheet_name="All tasks")


if __name__ == '__main__':
    main()
