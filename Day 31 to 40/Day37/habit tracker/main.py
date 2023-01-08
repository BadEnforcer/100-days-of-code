import requests
from datetime import datetime
today = datetime.now()
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
GRAPH_ENDPOINT = "https://pixe.la/v1/users/badenforcer/graphs"
GRAPH_ID = "python1234"
USERNAME = "badenforcer"
TOKEN = ""
user_params = {"token": {TOKEN},
               "username": {USERNAME},
               "agreeTermsOfService": "yes",
               "notMinor": "yes"}
graph_params = {"id": {GRAPH_ID},
                "name": "Python Test Graphs",
                "unit": "minutes",
                "type": "float",
                "color": "ajisai"
                }
header = {"X-USER-TOKEN": TOKEN}
date = today.strftime("%Y%m%d")
data = {
        "quantity": "100"
        }
# response = requests.post(url=GRAPH_ENDPOINT, json=graph_params, headers=header)
response = requests.delete(url=f"https://pixe.la/v1/users/badenforcer/graphs/{GRAPH_ID}/{date}",
                         headers=header)

print(response.text)
