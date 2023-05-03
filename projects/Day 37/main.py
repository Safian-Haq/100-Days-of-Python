import os

import requests
import datetime as dt


PIXELA_ENDPOINT = 'https://pixe.la/v1/users'
PIXELA_TOKEN = os.environ.get('PIXELA_TOKEN')
PIXELA_USERNAME = 'safianhaq'
PIXELA_GRAPH_ENDPOINT = PIXELA_ENDPOINT + f'/{PIXELA_USERNAME}/graphs'
PIXELA_GRAPH_ID = 'graph1'
PIXELA_POST_VALUE_ENDPOINT = PIXELA_ENDPOINT + f'/{PIXELA_USERNAME}/graphs/{PIXELA_GRAPH_ID}'


if __name__ == '__main__':

    # # Create a pixela user
    # params = {
    #     'token': PIXELA_TOKEN,
    #     'username': PIXELA_USERNAME,
    #     'agreeTermsOfService': 'yes',
    #     'notMinor': 'yes'
    # }
    #
    # response = requests.post(url=PIXELA_ENDPOINT,json=params)
    # response.raise_for_status()
    # print(response.text)

    # # Create graph
    # params_graph = {
    #     'id': PIXELA_GRAPH_ID,
    #     'name': 'Cycling Graph',
    #     'unit': 'Km',
    #     'type': 'float',
    #     'color': 'ajisai',
    #     'timezone': 'Asia/Karachi'
    # }
    #
    # headers = {
    #     'X-USER-TOKEN': PIXELA_TOKEN
    # }
    #
    # response = requests.post(url=PIXELA_GRAPH_ENDPOINT, json=params_graph, headers=headers)
    # response.raise_for_status()
    # print(response.text)

    # # POST a value into the graph
    # headers = { 'X-USER-TOKEN': PIXELA_TOKEN }
    #
    # params_post_value = {
    #     'date': dt.datetime.now().strftime('%Y%m%d'),
    #     'quantity': '10',
    # }
    #
    # response = requests.put(url=PIXELA_POST_VALUE_ENDPOINT, json=params_post_value, headers=headers)
    # response.raise_for_status()
    # print(response.text)

    # # PUT (Update) a value in the graph
    # PIXELA_PUT_VALUE_DATE = '20230129'
    #
    # PIXELA_PUT_VALUE_ENDPOINT = PIXELA_ENDPOINT + f'/{PIXELA_USERNAME}/graphs/{PIXELA_GRAPH_ID}/{PIXELA_PUT_VALUE_DATE}'
    #
    # headers = {'X-USER-TOKEN': PIXELA_TOKEN}
    #
    # params_post_value = {
    #     'quantity': '10'
    # }
    #
    # response = requests.put(url=PIXELA_PUT_VALUE_ENDPOINT, json=params_post_value, headers=headers)
    # response.raise_for_status()
    # print(response.text)

    PIXELA_PUT_VALUE_DATE = '20230129'

    PIXELA_DELETE_VALUE_ENDPOINT = PIXELA_ENDPOINT + f'/{PIXELA_USERNAME}/graphs/{PIXELA_GRAPH_ID}/{PIXELA_PUT_VALUE_DATE}'

    headers = { 'X-USER-TOKEN': PIXELA_TOKEN }

    response = requests.delete(url=PIXELA_DELETE_VALUE_ENDPOINT, headers=headers)
    response.raise_for_status()
    print(response.text)
