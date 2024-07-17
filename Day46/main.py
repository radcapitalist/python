
from datetime import date
from bs4 import BeautifulSoup
import os
import requests
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

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
print(f'{len(titles)}\n{titles}')

load_dotenv()

spotify_client_id = os.environ.get("SPOTIFY_CLIENT_ID")
spotify_secret = os.environ.get("SPOTIFY_CLIENT_SECRET")
spotify_redirect_uri = "http://example.com"

scope = "user-library-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=spotify_client_id,
                                               client_secret=spotify_secret,
                                               redirect_uri=spotify_redirect_uri,
                                               scope=scope))

results = sp.current_user_saved_tracks()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " - ", track['name'])

