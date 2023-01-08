import requests
from twilio.rest import Client
import os
from twilio.http.http_client import TwilioHttpClient

ENDPOINT = "http://api.openweathermap.org/data/2.5/forecast"
params = {"lat": 25.436298,
          "lon": 78.567352,
          "appid": ""}


# client = Client(account_sid=account_sid, password=auth_token, http_client=proxy_client)
client = Client(username=account_sid, password=auth_token)

response = requests.get(url=ENDPOINT, params=params)
response.raise_for_status()
data = response.json()["list"]
# print(data)

hourly_data = [forcast for forcast in data[:4]]

rain = False
heavy_rain = False
condition: str
for hour in hourly_data:
    if hour["weather"][0]["id"] < 600:
        rain = True
        break


# if rain:
message = client.messages.create(to="+917905179829",
                                     from_="+18145616566",
                                     body=f"Rain today☔⚠⚠⚠. Might be good to Bring an Umbrella ")

print(message.status)
