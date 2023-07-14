import requests
import os
from datetime import datetime
from dateutil.relativedelta import relativedelta

from flight_data import FlightData

header = {
    "apikey": os.environ["TEQUILA_API_KEY"],
}

tequila_location_endpoint = "https://api.tequila.kiwi.com/locations/query"
tequila_search_endpoint = "https://api.tequila.kiwi.com/search"
six_months = datetime.today() + relativedelta(months=+6)
return_from = datetime.today() + relativedelta(days=+7)
return_to = datetime.today() + relativedelta(days=+27)


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def get_destination_codes(self, cities):
        code = []
        for city in cities:
            tequila_params = {
                "term": city,
                'location_types': "airport"
            }

            response = requests.get(url=tequila_location_endpoint, params=tequila_params, headers=header)
            response.raise_for_status()
            code.append(response.json()['locations'][0]['city']['code'])
        return code

    def check_flight(self, flight_from, flight_to, from_time, to_time):
        tequila_params = {
            "fly_from": flight_from,
            "fly_to": flight_to,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP",
            "sort": "price"
        }

        response = requests.get(url=tequila_search_endpoint, params=tequila_params, headers=header)

        try:
            data = response.json()["data"][0]
        except IndexError:
            tequila_params["max_stopovers"] = 1
            response = requests.get(url=tequila_search_endpoint, params=tequila_params, headers=header)
            try:
                data = response.json()["data"][0]
            except IndexError:
                print(f"No Flights Found to {flight_to}.")
            else:
                flight_data = FlightData(
                    price=data["price"],
                    origin_city=data["route"][0]["cityFrom"],
                    origin_airport=data["route"][0]["flyFrom"],
                    destination_city=data["route"][0]["cityTo"],
                    destination_airport=data["route"][0]["flyTo"],
                    availability=data["availability"],
                    stop_over=1,
                    via_city=data['route'][0]['cityTo']
                )
                return flight_data
        else:
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                availability=data["availability"],
            )
            # print(f"{flight_data.destination_city}: £{flight_data.price}")
            return flight_data
