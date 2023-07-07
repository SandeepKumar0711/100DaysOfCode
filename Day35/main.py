import requests
from twilio.rest import Client

api_key ="Your_Weather_API_key"     #get free api key on https://www.weatherapi.com/
account_sid = 'AC90e0b0c8096752815b2d60f89bf298b3'
auth_token = 'Your Twilio authcode'  #get free auth token on https://console.twilio.com/


parameters = {
    "q": "Mumbai",
    "key": api_key,
}

response = requests.get(url="http://api.weatherapi.com/v1/forecast.json", params=parameters)
response.raise_for_status()

hourly_data = response.json()["forecast"]["forecastday"][0]["hour"]
sliced_data = hourly_data[:12]
will_rain = False
for hour_data in sliced_data:
    if hour_data['will_it_rain'] == 1:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='+18148015896',
        body='It is going to rain today, Bring your Umbrella☔☔',
        to='+918077434282'
    )

    print(message.status)