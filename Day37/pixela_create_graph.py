
import requests
from dotenv import load_dotenv
import os;

load_dotenv();

token = os.environ.get('PIXELA_TOKEN')
username = 'radcapitalist'

url_base = 'https://pixe.la/v1/users'
url_create_graph = f'{url_base}/{username}/graphs'

auth_header = 'X-USER-TOKEN'
graph_id = 'habit-tracker'
graph_name = 'Learning Python Tracker'
unit = 'minutes'
type = 'int'
color = 'ajisai'
timezone = 'America/New_York'
data = {
    "id": graph_id,
    "name": graph_name,
    "unit": unit,
    "type": type,
    "color": color,
    "timezone": timezone,
};
headers = {
    auth_header: token
}
response = requests.post(url=url_create_graph, json=data, headers=headers)
print(response.text)

# Graph url: https://pixe.la/v1/users/radcapitalist/graphs/habit-tracker'

