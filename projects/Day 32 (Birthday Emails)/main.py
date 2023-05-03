# import random
# import smtplib
# import datetime as dt
# import pandas as pd
# import calendar
#
# MY_EMAIL = 'sufian.python@gmail.com'
# PASSWORD = "crszpgiqykhtziup"
# DAY_OF_WEEK = 4
#
# with open('quotes.txt') as fp:
#     quotes_df = pd.read_csv(fp, sep= '" ', names=['quotes', 'author'], engine='python')
#
# if dt.datetime.now().weekday() == DAY_OF_WEEK:
#
#     weekday = list(calendar.day_abbr)[DAY_OF_WEEK] + 'day'
#
#     quote = random.choice(quotes_df['quotes'])
#     author = quotes_df[quotes_df.quotes == quote].values[0][1][2:]
#     quote = quote[1:]
#     print(f'{quote}\n{author}')
#
#     # Message
#     subject = f'{weekday} motivation'
#     message = subject + '\n\n' + f'{quote} \n\nFrom {author}'
#
#     with smtplib.SMTP('smtp.gmail.com') as connection:
#         print(connection.default_port)
#         connection.set_debuglevel(1)
#         connection.starttls()
#
#         connection.login(user=MY_EMAIL, password=PASSWORD)
#         connection.sendmail(
#             from_addr=MY_EMAIL, to_addrs='sufian_haq@live.com',
#             msg=f'Subject:{subject}\n\n{message}'
#         )
#


###########################################

import pandas as pd
import datetime as dt
import smtplib
import random

MY_EMAIL = 'sufian.python@gmail.com'
PASSWORD = "crszpgiqykhtziup"

# load birthdays
with open('birthdays.csv') as fp:
    df = pd.read_csv(fp)

# Isolate birthdays for today
today = dt.datetime.now()
today = (today.day, today.month)
target_birthdays = [row for index, row in df.iterrows() if today == (row['day'], row['month'])]

if len(target_birthdays) > 0:

    # Load letter templates
    letter_templates = []

    for i in range(1,4):
        with open(f'letter_templates/letter_{i}.txt') as fp:
            letter_templates.append(fp.readlines())

    # Connection to SMTP server
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.set_debuglevel(1)
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)

        # Send birthday messages
        for target in target_birthdays:

            # Choose a random letter template
            template = random.choice(letter_templates)

            # Update name in message
            template[0] = template[0].replace( '[NAME]', f'{target["name"]}')

            # Create final message
            message = ''.join(template)

            # Subject for the email
            subject = f'Happy Birthday!! {target["name"]}'

            # connection.sendmail(
            #             from_addr=MY_EMAIL, to_addrs=f'{target["email"]}',
            #             msg=f'Subject:{subject}\n\n{message}'
            #         )
