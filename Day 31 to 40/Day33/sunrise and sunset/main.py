import requests
from datetime import datetime

parameters = {
    "lat": 25.436298,
    "lng": 78.567352,
    "formatted": 0
}


response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()["results"]
sunrise = data["sunrise"].split("T")[1].split(":")[0]
sunset = data["sunset"].split("T")[1].split(":")[0]

time_now = datetime.now()

print(sunset)
print(sunrise)
print(time_now.hour)

