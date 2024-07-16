import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(url=URL)
movies_page = response.text
soup = BeautifulSoup(movies_page, 'html.parser')
movie_h3s = soup.find_all(name="h3", class_="title")
titles_worst_to_best = [movie.getText() for movie in movie_h3s]
titles_best_to_worst = titles_worst_to_best[::-1]
print(titles_best_to_worst)

with open("movie_rankings.txt", mode="w") as file:
    for movie in titles_best_to_worst:
        file.write(f"{movie}\n")


