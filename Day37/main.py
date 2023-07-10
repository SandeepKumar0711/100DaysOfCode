import requests
from datetime import datetime

USERNAME = "sandeep0711"
TOKEN = "as8fuas9dfhasfdjasd"

pixela_endpoint = "https://pixe.la/v1/users"

user_param = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_param)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": "graph1",
    "name": "Coding Hours",
    "unit": "hour",
    "type": "float",
    "color": "sora"
}

pixel_data_endpoint = f"{graph_endpoint}/{graph_config['id']}"

today = datetime.now()
pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "3.0",
}

headers = {
    "X-USER-TOKEN": TOKEN
}
#
# response = requests.post(url=pixel_data_endpoint, json=pixel_data, headers=headers)
# print(response.text)

update_endpoint = f"{pixel_data_endpoint}/{pixel_data['date']}"

update_data = {
    "quantity": "20"
}

# response = requests.put(url=update_endpoint, json=update_data, headers=headers)
# print(response.text)

response = requests.delete(url=update_endpoint, headers=headers)
print(response.text)