from constants import *
import requests

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):

        self.headers = {
            'apikey': API_KEY_TEQUILA
        }

    def search(self, adults: int, date_from: str, date_to: str, fly_from: str, fly_to: str,
               return_from: str, return_to: str, adult_hold_bag=1, adult_hand_bag=1,
               limit=3, **kwargs):

        parameters = {
            'adults': adults,
            'date_from': date_from,
            'date_to': date_to,
            'fly_from': fly_from,
            'fly_to': fly_to,
            'return_from': return_from,
            'return_to': return_to,
            'adult_hold_bag': adult_hold_bag,
            'adult_hand_bag': adult_hand_bag,
            'limit': limit
        }

        for key, value in kwargs:
            parameters[key] = value

        response = requests.get(url=API_ENDPOINT_TEQUILA, params=parameters, headers=self.headers)
        response.raise_for_status()
        data = response.json()
        messages = []
        for result in data['data']:
            message = f'Flight deal alert!\n' \
                      f'Price: {result["price"]}\n' \
                      f'Depart from: {result["flyFrom"]}\n' \
                      f'Arrival to: {result["flyTo"]}\n' \
                      f'Departure duration: {result["duration"]["departure"]}\n' \
                      f'Departure route: {len([flight for flight in result["route"] if flight["return"] == 0])}\n' \
                      f'Arrival duration: {result["duration"]["return"]}\n' \
                      f'Arrival route: {len([flight for flight in result["route"] if flight["return"] == 1])}\n' \
                      f'URL: {result["deep_link"]}'
            print(message)
            messages.append(message)
        return messages


if __name__ == '__main__':
    adults = 1
    date_from = '01/03/2023'  # DD/MM/YYYY
    date_to = '05/03/2023'
    return_from = '01/04/2023'
    return_to = '05/04/2023'
    fly_from = 'KHI'
    fly_to = 'LON'

    flight_search = FlightSearch()
    flight_search.search(adults=adults, date_from=date_from, date_to=date_to, fly_from=fly_from, fly_to=fly_to,
              return_from=return_from, return_to=return_to)

