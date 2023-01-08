import requests
# 'Authorization': os.environ["SHEETS_API_TOKEN"],
# constants
workout_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheets_endpoint = "https://api.sheety.co/5ee61503a85b9af8d9ededfffc2b9690/pythonWorkout/tvghvtcvtgct"
sheet_api_header = {"Content-Type": "application/json"}
nutritionix_header = {
    "x-app-id": "",
    "x-app-key": "",
    "x-remote-user-id": "0",
    "Content-Type": "application/json"
}

# query with the A.I.
user_input = input("So what did you do today?: ")
AI_response = requests.post(url=workout_endpoint, headers=nutritionix_header, json={"query": f"{user_input}"})
AI_response.raise_for_status()
# print(AI_response.json())

# posting the data into google sheets
for exercise in AI_response.json()['exercises']:
    contents = {"sheet1": {
        "date": f'{datetime.now().strftime("%d/%m/%Y")}',
        "time": f'{datetime.now().strftime("%H:%M:%S")}',
        "exercise": exercise['user_input'].title(),
        "duration": exercise["duration_min"],
        "calories": exercise["nf_calories"]
    }}
    sheet_api_req = requests.post(url=sheets_endpoint, headers=sheet_api_header, json=contents)
    sheet_api_req.raise_for_status()
    print(sheet_api_req.text)
import os
from datetime import datetime

# TODO: remove the keys before uploading to github
