# import requests
#
# response = requests.get('http://api.open-notify.org/iss-now.json')
#
# data = response.json()
#
# lat = response.json()['iss_position']['latitude']
# long = response.json()['iss_position']['longitude']
#
# iss_position = (long, lat)
# print(iss_position)
#
# from tkinter import *
# import requests
#
# def get_quote():
#
#     response = requests.get(url='https://api.kanye.rest/')
#     canvas.itemconfig(quote_text, text=response.json()['quote'])
#
#
#
# window = Tk()
# window.title("Kanye Says...")
# window.config(padx=50, pady=50)
#
# canvas = Canvas(width=300, height=414)
# background_img = PhotoImage(file="background.png")
# canvas.create_image(150, 207, image=background_img)
# quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 15, "bold"), fill="white")
# canvas.grid(row=0, column=0)
#
# kanye_img = PhotoImage(file="kanye.png")
# kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote, borderwidth=0)
# kanye_button.grid(row=1, column=0)
# get_quote()
#
#
# window.mainloop()
import datetime
import time
import smtplib
import requests

MY_LAT = 24.883714
MY_LONG = 67.080777
FROM_EMAIL = 'sufian.python@gmail.com'
FROM_EMAIL_PASSWORD = "crszpgiqykhtziup"
TO_EMAIL = 'sufian_haq@live.com'


def is_near(lat1: float, long1: float , lat2: float, long2: float):

    if lat1 - 5 <= lat2 <= lat1 + 5 and long1 -5 <= long2 <= long1 + 5:
        return True
    else:
        return False


def get_iss_location():

    iss_location_response = requests.get('http://api.open-notify.org/iss-now.json')
    iss_location_data = iss_location_response.json()
    lat = float(iss_location_data['iss_position']['latitude'])
    long = float(iss_location_data['iss_position']['longitude'])
    return long, lat

def send_email():

    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=FROM_EMAIL, password=FROM_EMAIL_PASSWORD)
        connection.sendmail(from_addr=FROM_EMAIL, to_addrs=TO_EMAIL,
                            msg='Subject:LOOKUP FOR ISS\n\nLookup to find the ISS in the sky.')


parameters = {'lat': str(MY_LAT) , 'long': str(MY_LONG), 'formatted' : '0'}

response = requests.get(url='https://api.sunrise-sunset.org/json', params=parameters)
response.raise_for_status()
data = response.json()

sunrise = int(data['results']['sunrise'].split('T')[1].split(':')[0])
sunset = int(data['results']['sunset'].split('T')[1].split(':')[0])


is_iss_over_me = False
while not is_iss_over_me:

    time_now = datetime.datetime.now().hour

    iss_location = get_iss_location()
    if is_near(iss_location[0], iss_location[1], MY_LAT, MY_LONG) and time_now < sunrise or time_now > sunset:
        print('Send email')
        send_email()
    else:
        print(f'iss_location: {iss_location} | my lat long: {MY_LAT, MY_LONG} |'
              f'  current hour: {time_now} | sunrise: {sunrise} | sunset: {sunset}')
    time.sleep(60)