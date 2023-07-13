import os
from twilio.rest import Client

account_sid = os.environ["ACCOUNT_SID"]
auth_token = os.environ["AUTH_TOKEN"]


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self, ):
        self.client = Client(account_sid, auth_token)

    def send_notification(self, message):
        message = self.client.messages.create(
            from_= os.environ["TWILIO_NUMBER"],
            body=message,
            to=os.environ["YOUR_NUMBER"]
        )

        print(message.status)