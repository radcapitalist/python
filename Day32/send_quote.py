
import smtplib
import datetime as dtlib
import os
from random import choice

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

SMTP_SERVER = "smtp-mail.outlook.com"
SMTP_SERVER_2 = "smtp.office365.com"
SMTP_PORT = 587
ENCRYPTION = "STARTTLS"
USER = "eric.hill@outlook.com"
APP_PASSWORD = "rodrrffqomckwbvz"
QUOTES_FILE = "quotes.txt"


def email_quote(quote): 
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as connection:
        connection.starttls()
        connection.login(user=USER, password=APP_PASSWORD)
        connection.sendmail(
            from_addr=USER, 
            to_addrs="ewh.online@outlook.com", 
            msg=f"Subject: Motivation quote!\n\n{quote}"
        )

now = dtlib.datetime.now()
if now.weekday() == 6:
    with open(file = QUOTES_FILE) as f:
        quotes = f.readlines()
        email_quote(choice(quotes))
