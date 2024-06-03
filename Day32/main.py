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

list_bdays = [{'name': row['name'], 'email': row.email, 'year': row.year, 'month': row.month, 'day': row.day}
              for (index, row) in birthday_data.iterrows()]

today = datetime.now()
month = today.month
day = today.day

for bday in list_bdays:
    if bday['month'] == month and bday['day'] == day:
        print(f"Sending birthday message to {bday['name']}")
        email_birthday_message(bday)
    else:
        print(f"This is not {bday['name']}\'s birthday")

