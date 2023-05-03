from constants import *
import smtplib


class NotificationManager:
    def send_message(self, message, to_addrs):
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)

            connection.sendmail(
                from_addr=MY_EMAIL, to_addrs=to_addrs,
                msg=f'Subject:Price alert\n\n{message}'
            )