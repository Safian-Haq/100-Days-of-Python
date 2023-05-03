from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

if __name__ == '__main__':
    DM = DataManager()
    bucket_list = DM.get_data()

    f_search = FlightSearch()
    NM = NotificationManager()

    adults = 1
    date_from = '01/03/2023'  # DD/MM/YYYY
    date_to = '05/03/2023'
    return_from = '01/04/2023'
    return_to = '05/04/2023'
    fly_from = 'KHI'

    for item in bucket_list:
        fly_to = item['iataCode']
        messages = f_search.search(adults=adults, date_from=date_from, date_to=date_to, return_from=return_from, return_to=return_to,
                        fly_from=fly_from, fly_to=fly_to)

        for msg in messages:
            NM.send_message(msg, 'sufian_haq@live.com')
