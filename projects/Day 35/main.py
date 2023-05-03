import requests
from twilio.rest import Client
import os

API_KEY = os.environ.get('TWILIO_API_KEY')
TWILIO_SID = 'AC5b6f6c8c0777cf125692a852d7410381'
TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')
MESSAGING_SERVICE_SID = 'MG3a449e11e17cc8e6a295f2a057dd788b'
SEND_TO_PHONE_NUMBER = os.environ.get('MY_PHONE_NUMBER')

MY_LAT = '24.883698'
MY_LONG = '67.080715'

MY_LAT = '3.793532'
MY_LONG = '101.857468'

API_ENDPOINT = 'https://api.openweathermap.org/data/3.0/onecall'

PARAMETERS = {'lat': MY_LAT, 'lon': MY_LONG, 'appid': API_KEY,
              'exclude': 'current,minutely,daily'}

response = requests.get(url=API_ENDPOINT, params=PARAMETERS)
response.raise_for_status()
weather_data = response.json()['hourly'][:12]

will_rain = False
for hr_data in weather_data:
    if hr_data['weather'][0]['id'] < 700:
        will_rain = True
if will_rain:
    tw_client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    tw_message = tw_client.messages.create(
        messaging_service_sid=MESSAGING_SERVICE_SID,
        body="It's going to rain today.",
        to=SEND_TO_PHONE_NUMBER
    )

    print(tw_message.sid)
