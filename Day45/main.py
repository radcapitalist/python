
from bs4 import BeautifulSoup
import os
import requests

# abspath = os.path.abspath(__file__)
# dname = os.path.dirname(abspath)
# os.chdir(dname)

# HTML_FILE = 'website.html'

# with open(file=HTML_FILE, mode='r') as htmlfile:
#     content = htmlfile.read()
# print(content)

# soup = BeautifulSoup(content, 'html.parser')
# print(soup.title.name)
# print(soup.title.string)

# aTags = soup.find_all(name='a')
# print('anchor tags')
# for tag in aTags:
#     # two ways to get an attribute value
#     print(tag.attrs['href'])
#     print(tag.get('href'))

# name_h1 = soup.find(name='h1', id='name')
# print(name_h1.string)

# headings = soup.find_all(class_='heading')
# print(headings)
# for heading in headings:
#     print(heading.string)

# # CSS selectors
# company_url = soup.select_one(selector='p a')
# print(company_url)

# print()

# headings = soup.select('.heading')
# print(headings)

HN_URL='https://news.ycombinator.com/news'

response = requests.get(url=HN_URL)
hn_page = response.text
soup = BeautifulSoup(hn_page, 'html.parser')
articles = soup.select('tr.athing td span.titleline a')
points = soup.select('span.score')
print(f'articles: {len(articles)}   points: {len(points)}')

article_links = []
article_text = []
article_upvotes = []

for index in range(0, len(articles)):
    article = articles[index]
    if not 'from?site' in article.get('href'):
        print(article.getText())
        article_text.append(article.getText())
        article_links.append(article.get('href'))

for pindex in range(0, len(points)):
    point_string = points[pindex].text
    parts = point_string.split(' ')
    article_upvotes.append(int(parts[0]))

while len(article_upvotes) < len(article_links):
    article_upvotes.append(42)

# print(article_links)
# print(article_text)
# print(article_upvotes)
print(f'articles: {len(article_links)}  upvotes: {len(article_upvotes)}')


