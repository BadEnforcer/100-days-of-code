import smtplib


with smtplib.SMTP("smtp-mail.outlook.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_pass)
    connection.sendmail(from_addr=my_email,
                        to_addrs="rajdwivedipc@gmail.com",
                        msg="Subject:test!!!\n\nThis Shit Works")
