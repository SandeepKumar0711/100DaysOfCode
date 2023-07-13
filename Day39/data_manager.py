import requests

sheety_endpoint = "https://api.sheety.co/66547ba5b44e8046f5235fd78eec73a5/flightDeals/prices"


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=sheety_endpoint)
        self.destination_data = response.json()["prices"]
        # print(self.destination_data)
        return self.destination_data
    def update_destination_codes(self):
        for code in self.destination_data:
            parameter = {
                "price": {
                    "iataCode": code['iataCode']
                }
            }
            response = requests.put(url=f"{sheety_endpoint}/{code['id']}", json=parameter)
            response.raise_for_status()