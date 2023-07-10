import requests
from datetime import datetime
import os


GENDER = "male"
WEIGHT_KG = 75
HEIGHT_CM = 5.11
AGE = 22


APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]

api_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
data = {
    "query": input('Tell me which exercises you did:'),
}

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

response = requests.post(url=api_endpoint, json=data, headers=headers)
data = response.json()["exercises"][0]

sheet_input = {
    "workout": {
        "exercise": data["name"].title(),
        "duration": data["duration_min"],
        "calories": data["nf_calories"],
        "date": datetime.now().strftime("%d/%m/%Y"),
        "time": datetime.now().strftime("%H:%M:%S")
    }
}

sheety_endpoint = "https://api.sheety.co/9c5a8b967016de481df8792339427501/myWorkouts/workouts"

headers = {
    "Authorization": os.environ["AUTH_CODE"]
}
response = requests.post(url=sheety_endpoint, json=sheet_input, headers=headers)
print(response.json())