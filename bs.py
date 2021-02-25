import requests
from bs4 import BeautifulSoup

page= requests.get('https://namu.wiki/w/%EC%9A%95%EC%84%A4/%ED%95%9C%EA%B5%AD%EC%96%B4')

soup= BeautifulSoup(page.content, 'html.parser')

para=soup.find_all('div', class_='wiki-paragraph')
words = soup.find_all('a', class_='wiki-link-internal')

print(soup.prettify())