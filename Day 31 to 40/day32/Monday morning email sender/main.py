import datetime as dt
from random import choice
import smtplib

now = dt.datetime.now()
day_of_week = now.isoweekday()


if day_of_week == 1:  # monday  # testing
    with open("quotes.txt", mode="r") as file:
        data = file.readlines()
        quote = choice(data)

        with smtplib.SMTP("smtp-mail.outlook.com") as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASS)
            connection.sendmail(from_addr=EMAIL,
                                to_addrs="",
                                msg=f"Subject:Your Daily Motivation\n\n{quote}")

            # we can also send it to ourselves
