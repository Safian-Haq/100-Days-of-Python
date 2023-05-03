import requests
import datetime as dt
from pandas.tseries.offsets import BDay
import contextlib
from urllib.parse import urlencode
from urllib.request import urlopen
import os

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# Alpha Vantage Stocks API
API_KEY_STOCK = os.environ.get('ALPHAVANTAGE_API_KEY')
API_ENDPOINT_STOCK = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED'

# NewsAPI
API_KEY_NEWS = os.environ.get('NEWS_API_KEY')
API_ENDPOINT_NEWS = 'https://newsapi.org/v2/everything?'

# Twilio
TWILIO_SID = 'AC5b6f6c8c0777cf125692a852d7410381'
TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')
MESSAGING_SERVICE_SID = 'MG3a449e11e17cc8e6a295f2a057dd788b'
SEND_TO_PHONE_NUMBER = os.environ.get('MY_PHONE_NUMBER')

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.


#Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""


def get_last_2_day():
    last_business_day = dt.datetime.today() - BDay(1)
    second_last_business_day = dt.datetime.today() - BDay(2)

    last_business_day = '-'.join(
        (f'{last_business_day.year}', f'{last_business_day.month:02d}', f'{last_business_day.day:02d}')
    )
    second_last_business_day = '-'.join(
        (f'{second_last_business_day.year}', f'{second_last_business_day.month:02d}', f'{second_last_business_day.day:02d}')
    )

    return last_business_day, second_last_business_day

def make_tiny(url):
    request_url = ('http://tinyurl.com/api-create.php?' + urlencode({'url':url}))
    with contextlib.closing(urlopen(request_url)) as response:
        return response.read().decode('utf-8 ')


if __name__ == '__main__':

    # Get stock data
    params_stock = {
        'symbol': STOCK,
        'apikey': API_KEY_STOCK,
    }

    response = requests.get(url=API_ENDPOINT_STOCK, params=params_stock)
    response.raise_for_status()
    data = response.json()['Time Series (Daily)']

    # Calculate percent difference for last 2 business days
    target_days = get_last_2_day()
    last_day_close = float(data[target_days[0]]['4. close'])
    second_last_day_close = float(data[target_days[1]]['4. close'])

    percent_diff = (last_day_close - second_last_day_close)/last_day_close * 100

    # If percentage difference is greater than +/- 5, send text
    if abs(percent_diff) >= 5:

        # Get articles for NewsAPI for specified Stock
        params_news = {
            'apiKey': API_KEY_NEWS,
            'q': COMPANY_NAME,
            'pageSize': 3,
            'sortBy': 'popularity',
            'searchIn': 'title',
            'language': 'en'
        }

        response_news = requests.get(url=API_ENDPOINT_NEWS, params=params_news)
        response_news.raise_for_status()
        data = response_news.json()

        # Setup Twilio connection
        # tw_client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

        # Send a seperate message for each article from twilio
        for article in data['articles']:

            tiny = make_tiny(article['url'])

            message = f'{STOCK} {round(percent_diff, 2)}\n' \
                      f'Headline: {article["title"]}\n' \
                      f'{tiny}'
            print(message)
            # tw_message = tw_client.messages.create(
            #     messaging_service_sid=MESSAGING_SERVICE_SID,
            #     body=message,
            #     to=SEND_TO_PHONE_NUMBER
            # )
            #
            # print(tw_message.sid)
