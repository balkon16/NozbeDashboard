import json

import requests

with open("src/credentials/token.json") as f:
    token = json.load(f)["token"]

BASE_URL = "https://api.nozbe.com:3000"
endpoint = "/list"
url = BASE_URL + endpoint

data = {
    "type": "project"
}


headers = {
    "Authorization": token
    # "Authorization": f"Bearer {token}",  # Assuming Bearer token authentication
    # "Content-Type": "application/json"  # Indicate JSON data
}

resp = requests.get(
    url=url,
    data=data,
    headers=headers
)
# print("After request.")
for project_data in resp.json():
    print(project_data["name"])
