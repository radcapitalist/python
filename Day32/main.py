##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import os
import csv
import pandas
import smtplib
from random import randint
from datetime import datetime

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

SMTP_SERVER = "smtp-mail.outlook.com"
SMTP_SERVER_2 = "smtp.office365.com"
SMTP_PORT = 587
ENCRYPTION = "STARTTLS"
USER = "eric.hill@outlook.com"
APP_PASSWORD = "rodrrffqomckwbvz"

def get_birthday_message(name):
    msg_num = randint(1, 3)
    path = f'./letter_templates/letter_{msg_num}.txt'
    with open(file=path) as msg_file:
        msg = msg_file.read()
    msg = msg.replace('[NAME]', name)
    return msg

def email_birthday_message(bday_rec):
    print(f"Sending birthday message to {bday_rec['name']}")
    msg = get_birthday_message(bday_rec['name'])
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as connection:
        connection.starttls()
        connection.login(user=USER, password=APP_PASSWORD)
        connection.sendmail(
            from_addr=USER, 
            to_addrs=bday_rec['email'],
            msg=f"Subject: Happy Birthday!\n\n{msg}"
        )

BD_FNAME = 'birthdays.csv'
birthday_data = pandas.read_csv(BD_FNAME)

today = datetime.now()
month = today.month
day = today.day

# list_bdays = [{'name': data_row['name'], 'email': data_row.email, 'year': data_row.year, 'month': data_row.month, 'day': data_row.day}
#               for (index, data_row) in birthday_data.iterrows()]


# for bday in list_bdays:
#     if bday['month'] == month and bday['day'] == day:
#         print(f"Sending birthday message to {bday['name']}")
#         #email_birthday_message(bday)
#     else:
#         print(f"This is not {bday['name']}\'s birthday")

birthday_dict = {(data_row.month, data_row.day): data_row
                 for (index, data_row) in birthday_data.iterrows()}

for key, value in birthday_dict.items():
    print(value["name"])

if (month, day) in birthday_dict:
    bday_row = birthday_dict[(month, day)]
    email_birthday_message(bday_row)
