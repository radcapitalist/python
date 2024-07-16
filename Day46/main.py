
from datetime import date
from bs4 import BeautifulSoup
import os
import requests

H100_URL_BASE = 'https://www.billboard.com/charts/hot-100/'

# Input a date as a string, split it and create a date object
#date_entry = input('Enter a date in m/d/y format (four-digit year): ')
date_entry = '6/15/2013'
month, day, year = map(int, date_entry.split('/'))
sel_date = date(year, month, day)
print(sel_date)

URL = f"{H100_URL_BASE}{sel_date}"
print(URL)

response = requests.get(url=URL)
hot_100_page = response.text
soup = BeautifulSoup(hot_100_page, 'html.parser');
song_h3s = soup.select('div.o-chart-results-list-row-container li.o-chart-results-list__item h3#title-of-a-story')
titles = [song.getText().strip() for song in song_h3s]
print(titles)
artist_spans = soup.select('div.o-chart-results-list-row-container li.o-chart-results-list__item span')
