from constants import *
import requests

class DataManager:
    #This class is responsible for talking to the Google Sheet.

    def get_data(self):
        response = requests.get(url=API_ENDPOINT_SHEETY)
        response.raise_for_status()
        return response.json()['sheet1']


if __name__ == '__main__':
    DM = DataManager()
    print(DM.get_data())

