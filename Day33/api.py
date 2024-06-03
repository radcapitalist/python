
import requests

endpoint = "http://api.open-notify.org/iss-now.json"
response = requests.get(url=endpoint)
response.raise_for_status()

latitude = response.json()["iss_position"]["latitude"]
longitude = response.json()["iss_position"]["longitude"]
location = (longitude, latitude)

print(location)