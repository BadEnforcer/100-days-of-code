import smtplib

from pandas import read_csv
from random import choice
import datetime as dt

BD_DATA = read_csv("birthdays.csv")
all_letters = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]

SMTP_ADDRESS = "smtp-mail.outlook.com"


current_time = dt.datetime.now()
today = dt.datetime(year=2000, month=current_time.month, day=current_time.day)
print(today)


for name in BD_DATA["name"]:
    year = BD_DATA.loc[BD_DATA['name'] == name, 'year'].item()

    person = dt.datetime(year=2000,
                         month=BD_DATA.loc[BD_DATA['name'] == name, 'month'].item(),
                         day=BD_DATA.loc[BD_DATA['name'] == name, 'day'].item())
    # print(person)
    if today == person:
        with open(f"letter_templates/{choice(all_letters)}") as file:
            data = file.read()
            letter_content = data.replace("[NAME]", name)
            print(letter_content)

        with smtplib.SMTP(SMTP_ADDRESS) as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASS)
            connection.sendmail(from_addr=EMAIL,
                                to_addrs=BD_DATA.loc[BD_DATA['name'] == name, 'email'].item(),
                                msg=f"Subject:Happy Birthday!!\n\n{letter_content}")
            print(f"Email sent! to {name} at {dt.datetime.now()}")
