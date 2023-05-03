import os

import requests
import datetime as dt

API_ID = 'b0253440'
API_KEY = os.environ.get('NUTRITIONIX')
API_ENDPOINT = 'https://trackapi.nutritionix.com/v2/natural/exercise'

SHEETY_ENDPOINT = 'https://api.sheety.co/e78bb427cabeb29c63596fc4b1bc996a/day38/sheet1'

headers = {
    'x-app-id': API_ID,
    'x-app-key': API_KEY
}
#
# params = {
#     'query': 'ran for 5 km'
# }
#
# response = requests.post(url=API_ENDPOINT, json=params, headers=headers)
# response.raise_for_status()

user_input = input("Tell me which exercises you did: ")

params = {
    'query': user_input
}

response = requests.post(url=API_ENDPOINT, json=params, headers=headers)
response.raise_for_status()
data = response.json()


headers_sheety = {
    "Authorization": os.environ.get("SHEETY_AUTH")
}
for ex in data['exercises']:
    print(ex)

    row = {
        "sheet1": {
            "date": dt.datetime.now().strftime("%d/%m/%Y/"),
            "time": dt.datetime.now().strftime("%X"),
            "exercise": ex['name'].capitalize(),
            "duration": ex['duration_min'],
            "calories": ex['nf_calories']
        }
    }
    print(row)
    response = requests.post(url=SHEETY_ENDPOINT, json=row, headers=headers_sheety)
    response.raise_for_status()
    print(response.json())
