

import requests
from dotenv import load_dotenv
import os;
from datetime import datetime

load_dotenv();

username = 'radcapitalist'
graph_id = 'habit-tracker'

url_base = 'https://pixe.la/v1/users'
url_add_pixel = f'{url_base}/{username}/graphs/{graph_id}'

auth_header = 'X-USER-TOKEN'
token = os.environ.get('PIXELA_TOKEN')
headers = {
    auth_header: token
}

today = datetime.now()
month = '{:02d}'.format(today.month)
day = '{:02d}'.format(today.day)
today_str = f'{today.year}{month}{day}'
in_date = input(f'Date to add pixel for (blank for today ({today_str})): ')
if in_date == '':
    in_date = today_str
else:
    # could parse in_date and make sure it's in range here
    pass

real_date = datetime.strptime(in_date, '%Y%m%d')
formatted_date = real_date.strftime('%Y-%m-%d')
in_value = int(input(f'Enter pixel value for {formatted_date}: '))

print(f"Adding pixel with value {in_value} for date {formatted_date}")

data = {
    "date": in_date,
    "quantity": str(in_value),
}
response = requests.post(url=url_add_pixel, json=data, headers=headers)
print(response.text)

# Graph url: https://pixe.la/v1/users/radcapitalist/graphs/habit-tracker'
