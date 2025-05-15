import json
import logging
import requests

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class NozbeAPIClient:
    """
    A client for interacting with the Nozbe REST API.
    """

    def __init__(self, token_file="src/credentials/token.json", base_url="https://api.nozbe.com:3000"):
        """
        Initializes the NozbeAPIClient with the API token and base URL.

        Args:
            token_file (str): Path to the JSON file containing the API token.
            base_url (str): The base URL of the Nozbe API.
        """
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

    def _get_data(self, endpoint, data=None):
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

    def get_entity(self, entity_type):
        """
        Fetches a list of entities from the API based on the entity type.

        Args:
            entity_type (str): The type of entity to fetch (e.g., "project", "task").

        Returns:
            list: A list of dictionaries, where each dictionary represents an entity.

        Raises:
            NotImplementedError: If the entity type is not supported.
        """
        if entity_type == "project":
            return self.get_projects()
        elif entity_type == "task":
            return self.get_tasks()
        else:
            logging.error(f"Unsupported entity type: {entity_type}")
            raise NotImplementedError(f"Unsupported entity type: {entity_type}")
