
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
articles = soup.select('tr td span.titleline a')
points = soup.select('span.score')
print(f'articles: {len(articles)}   points: {len(points)}')

for article in articles:
    if not 'from?site' in article.get('href'):
        article_text = article.getText()
        article_link = article.get('href')
        print(f'{article_text}  [{article_link}]')



