import smtplib
import datetime as dt
import pandas
import random

LETTER_LIST = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
PLACEHOLDER = "[NAME]"
my_email = "yourmail@test.com"
password = "yourpassword"

now = dt.datetime.now()
current_day = now.day
current_month = now.month


current_date = f"{current_day}-{current_month}"

data = pandas.read_csv("birthdays.csv")
new = data.to_dict(orient="records")
for i in new:
    birth_day = i["day"]
    birth_month = i["month"]
    birth_date = f"{birth_day}-{birth_month}"
    if current_date == birth_date:
        template_name = random.choice(LETTER_LIST)
        with open(f"letter_templates/{template_name}") as letter:
            letter_contents = letter.read()
            new_letter = letter_contents.replace(PLACEHOLDER, i["name"])
        with smtplib.SMTP("smtp.test.com") as connection:  # stmp info of your mail provider
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=i["email"], msg=f"Subject: Happy Birthday\n\n{new_letter}")