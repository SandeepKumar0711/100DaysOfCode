import os
from twilio.rest import Client
import smtplib

account_sid = os.environ["ACCOUNT_SID"]
auth_token = os.environ["AUTH_TOKEN"]
MY_EMAIL = os.environ["EMAIL"]
MY_PASSWORD = os.environ["PASSWORD"]

class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self, ):
        self.client = Client(account_sid, auth_token)

    def send_notification(self, message):
        # message = self.client.messages.create(
        #     from_= os.environ["TWILIO_NUMBER"],
        #     body=message,
        #     to=os.environ["YOUR_NUMBER"]
        # )

        print(message)

    def send_emails(self, emails, message):
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}".encode('utf-8')
                )
