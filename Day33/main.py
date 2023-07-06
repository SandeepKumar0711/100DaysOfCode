import smtplib
import requests
from datetime import datetime
import time

MY_LAT = 28.466591
MY_LONG = 77.033310
MY_EMAIL = "test@mail.com"
PASSWORD = "your password"


def within_range():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    data = response.json()["iss_position"]
    iss_longitude = float(data["longitude"])
    iss_latitude = float(data["latitude"])
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True
    return False


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    time_now = datetime.now().hour
    if time_now >= sunset or time_now <= sunrise:
        return True


while True:
    time.sleep(60)
    if is_night() and within_range():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs="test2@mail.com", msg="Subject:Look Up\n\nThe ISS is "
                                                                                   "above you in the sky.")