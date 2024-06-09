
import requests
import dateutil.parser as parser
from datetime import datetime, timezone
import smtplib
import time

iss_endpoint = "http://api.open-notify.org/iss-now.json"
sun_endpoint = "https://api.sunrise-sunset.org/json"

MY_LAT = 35.7197
MY_LONG = -78.8439
MARGIN = 3
LAT_LB = MY_LAT - MARGIN
LAT_UB = MY_LAT + MARGIN
LONG_LB = MY_LONG - MARGIN
LONG_UB = MY_LONG + MARGIN
SMTP_SERVER = "smtp-mail.outlook.com"
SMTP_SERVER_2 = "smtp.office365.com"
SMTP_PORT = 587
ENCRYPTION = "STARTTLS"
USER = "eric.hill@outlook.com"
APP_PASSWORD = "rodrrffqomckwbvz"
EXEC_EVERY = 60.0

def get_iss_position():
    position = None
    try:
        response = requests.get(url=iss_endpoint)
    except Exception:
        response = None
    
    if not response is None and response.status_code == 200:
        latitude = float(response.json()["iss_position"]["latitude"])
        longitude = float(response.json()["iss_position"]["longitude"])
        position = {
            "lat": longitude, 
            "lng": latitude,
            "is_overhead": False,
        }
        if latitude > LAT_LB and latitude < LAT_UB and longitude > LONG_LB and longitude < LONG_UB:
            position["is_overhead"] = True
    else:
        print("Unable to get ISS position just now.")

    return position

  
def make_params(longitude, latitude):
    return {
        "lat": latitude,
        "lng": longitude,
        "tzid": "America/New_York",
        "formatted": 0,
    }

def is_it_nighttime():
    is_nighttime = False
    params = make_params(latitude = MY_LAT, longitude = MY_LONG)
    response = requests.get(url=sun_endpoint, params = params)
    if (response.status_code == 200):
        data = response.json()
        utc_sunrise = data["results"]["sunrise"]
        utc_sunset = data["results"]["sunset"]
        dt_sunrise = parser.parse(utc_sunrise)
        dt_sunset = parser.parse(utc_sunset)
    else:
        print("Unable to get sunrise/sunset values just now.")

    now = datetime.now(timezone.utc)
    if now < dt_sunrise or now > dt_sunset:
        is_nighttime = True

    return is_nighttime

def send_iss_overhead_email(lng, lat):
    msg = f"The ISS is overhead! Current position: longitude: {lng}, latitude: {lat}"
    to = USER
    subject = "The ISS is overhead!"
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as connection:
        connection.starttls()
        connection.login(user=USER, password=APP_PASSWORD)
        connection.sendmail(
            from_addr=USER,
            to_addrs=[to],
            msg = "From: %s\n" % USER
                + "To: %s\n" % to
                + "Subject: %s\n" % subject
                + "\n"
                + msg
        )

def check():
    position = get_iss_position()
    if not position is None:
        print(f"ISS position: longitude: {position['lng']}, latitude: {position['lat']}")
        if position["is_overhead"] == True and is_it_nighttime():
            print("The ISS is overhead and it's dark!")
            send_iss_overhead_email(lng=position["lng"], lat=position["lat"])
        else:
            print("The ISS is NOT overhead or it's not dark.")
        print()

print()
starttime = time.monotonic()
while True:
    print('tick')
    check()
    time.sleep(EXEC_EVERY - ((time.monotonic() - starttime) % EXEC_EVERY))
