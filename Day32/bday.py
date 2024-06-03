
import smtplib
import datetime as dtlib

SMTP_SERVER = "smtp-mail.outlook.com"
SMTP_SERVER_2 = "smtp.office365.com"
SMTP_PORT = 587
ENCRYPTION = "STARTTLS"
USER = "eric.hill@outlook.com"
APP_PASSWORD = "rodrrffqomckwbvz"

# with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as connection:
#     connection.starttls()
#     connection.login(user=USER, password=APP_PASSWORD)
#     connection.sendmail(
#         from_addr=USER, 
#         to_addrs="ewh.online@outlook.com", 
#         msg="Subject: SMTP\n\nThis is my first e-mail!", )

now = dtlib.datetime.now()
print(now)
year = now.year
month = now.month
day = now.day
print(f'{now.weekday()}, {month}/{day}/{year}')

mydt = dtlib.datetime(year=1962, month=7, day=5)
print(mydt)
