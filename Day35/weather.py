
import requests

OPENWEATHER_APIKEY = "4b68cfd1fc753ba8d4ea8f6575acaa1c"

MY_LAT = 35.7197
MY_LONG = -78.8439
open_weather_url = 'https://api.openweathermap.org/data/3.0/onecall'

def make_params():
    return {
        "lat": MY_LAT,
        "lon": MY_LONG,
        "appid": OPENWEATHER_APIKEY,
        "exclude": ['minutely'],
        "units": 'standard',
    }

def get_weather():
    weather = None
    params = make_params()
    response = requests.get(url=open_weather_url, params=params)
    response.raise_for_status()
    if response.status_code == 200:
        weather = response.data
    return weather

print(get_weather())
