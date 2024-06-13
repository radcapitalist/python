
import requests
from dotenv import load_dotenv
import os;

load_dotenv();

token = os.environ.get('PIXELA_TOKEN')
url_base = 'https://pixe.la/v1'
url_create_account = url_base + '/users'
data = {
    "token": token,
    "username": "radcapitalist",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
};
response = requests.post(url=url_create_account, json=data)
print(response.text)
