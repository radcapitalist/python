
import dateutil.parser
import requests
from datetime import datetime
import dateutil

url = "https://api.sunrise-sunset.org/json"

def make_params(longitude, latitude):
    return {
        "lat": latitude,
        "lng": longitude,
        "tzid": "America/New_York",
        "formatted": 0,
    }

params = make_params(latitude = 35.7197, longitude = -78.8439)

response = requests.get(url=url, params = params)
response.raise_for_status()
print(response.url)
data = response.json()
utc_sunrise = data["results"]["sunrise"]
utc_sunset = data["results"]["sunset"]
dt_sunrise = dateutil.parser.parse(utc_sunrise)
dt_sunset = dateutil.parser.parse(utc_sunset)
print(f"rise: {dt_sunrise}, set: {dt_sunset}")

print(datetime.now())
