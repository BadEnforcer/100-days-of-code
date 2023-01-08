import smtplib
import time
import requests
from datetime import datetime

MY_LAT = 25.454498  # Your latitude
MY_LONG = 78.636332  # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])


def is_iss_close():
    if MY_LAT + 5 >= iss_latitude >= MY_LAT - 5:
        if MY_LONG + 5 >= iss_longitude >= MY_LONG - 5:
            return True
        else:
            return False
    else:
        return False


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
time_now = datetime.now()


def is_night():
    if sunrise > time_now.hour > sunset:
        return True
    else:
        return False


def send_mail():
    with smtplib.SMTP("smtp-mail.outlook.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(to_addrs=EMAIL, from_addr=EMAIL, msg="Subject:Look in the Sky!!!\n\n"
                                                                 f"The ISS is above you right now!, come out and "
                                                                 f"see!\n{time_now.now()}")
        print(f"Email sent on {time_now.hour}")


# If the ISS is close to my current position
while True:
    if is_iss_close() and is_night():
        send_mail()
        print("waiting for 60 seconds")
        time.sleep(360)
    else:
        print("Not here yet!")
        time.sleep(60)

# BONUS: run the code every 60 seconds.
