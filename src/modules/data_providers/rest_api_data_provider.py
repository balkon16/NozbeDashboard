import json
import logging
import requests

from modules.data_providers.abstract_data_provider import DataProvider


class RestAPIDataProvider(DataProvider):
    """
    A client for interacting with the Nozbe REST API.
    """

    def __init__(self, token_file="src/credentials/token.json"
                 , base_url="https://api.nozbe.com:3000"
                 , log_level=logging.INFO):
        """
        Initializes the NozbeAPIClient with the API token and base URL.

        Args:
            token_file (str): Path to the JSON file containing the API token.
            base_url (str): The base URL of the Nozbe API.
        """
        super().__init__(log_level)
        self.base_url = base_url
        self.token = self._load_token(token_file)
        self.headers = {"Authorization": self.token}  # Assuming simple token authentication

    def _load_token(self, token_file):
        """
        Loads the API token from the specified JSON file.

        Args:
            token_file (str): Path to the JSON file containing the API token.

        Returns:
            str: The API token.
        """
        try:
            with open(token_file) as f:
                token = json.load(f)["token"]
            logging.info(f"Token loaded successfully from {token_file}")
            return token
        except FileNotFoundError:
            logging.error(f"Token file not found: {token_file}")
            raise FileNotFoundError(f"Token file not found: {token_file}")
        except json.JSONDecodeError:
            logging.error(f"Invalid JSON format in token file: {token_file}")
            raise json.JSONDecodeError(f"Invalid JSON format in token file: {token_file}", "", 0)
        except KeyError:
            logging.error(f"Token key not found in token file: {token_file}")
            raise KeyError(f"Token key not found in token file: {token_file}")

    def _get_data(self, endpoint, url_params="", data=None):
        """
        Fetches data from the specified API endpoint.

        Args:
            endpoint (str): The API endpoint to fetch data from.
            data (dict, optional): The data to send with the request. Defaults to None.

        Returns:
            list: A list of dictionaries containing the fetched data.

        Raises:
            requests.exceptions.RequestException: If the API request fails.
        """

        url = self.base_url + endpoint
        if url_params:
            url += "?" + url_params

        try:
            logging.info(f"Sending GET request to {url} with data: {data}")
            response = requests.get(url, headers=self.headers, params=data)  # Use params for GET requests
            response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
            logging.info(f"Received response with status code: {response.status_code}")
            return response.json()
        except requests.exceptions.RequestException as e:
            logging.error(f"API request failed: {e}")
            raise

    def get_projects(self):
        """
        Fetches a list of projects from the API.

        Returns:
            list: A list of dictionaries, where each dictionary represents a project.
        """
        endpoint = "/list"
        data = {"type": "project"}
        return self._get_data(endpoint, data)

    def get_tasks(self):
        """
        Fetches a list of tasks from the API.

        Returns:
            list: A list of dictionaries, where each dictionary represents a task.
        """
        endpoint = "/list"
        data = {"type": "task"}
        return self._get_data(endpoint, data)

    def get_tasks_for_project(self):
        endpoint = "/tasks"

        # https://api4.nozbe.com/v1/api/tasks?limit=1000&offset=0&project_id=x1aNvN70qlVBV61i
        return self._get_data(endpoint, url_params="limit=1000&project_id=x1aNvN70qlVBV61i") # TODO: pass URL params as dict
