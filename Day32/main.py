##################### Extra Hard Starting Project ######################

import os
import pandas
import smtplib
#import telepot
from random import randint
from datetime import datetime

#telepot.api.set_proxy('http://proxy.server:3128')

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
    to = bday_rec['email']
    cc = USER
    subject = "Happy Birthday!"
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as connection:
        connection.starttls()
        connection.login(user=USER, password=APP_PASSWORD)
        connection.sendmail(
            from_addr=USER,
            to_addrs=[to] + [cc],
            msg = "From: %s\n" % USER
                + "To: %s\n" % to
                + "CC: %s\n" % cc
                + "Subject: %s\n" % subject
                + "\n"
                + msg
        )

BD_FNAME = 'birthdays.csv'
birthday_data = pandas.read_csv(BD_FNAME)

today = datetime.now()
month = today.month
day = today.day

birthday_dict = {(data_row.month, data_row.day): data_row
                 for (index, data_row) in birthday_data.iterrows()}

if (month, day) in birthday_dict:
    bday_row = birthday_dict[(month, day)]
    email_birthday_message(bday_row)
else:
    print('Nobody found with a birthday today.')
