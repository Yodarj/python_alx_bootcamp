from requests import get
from bs4 import BeautifulSoup




url = "https://helion.pl/search?qa=&serwisyall=&szukaj=python&wprzyg=&wsprzed=&wyczerp="

responce = get(url)

html_soup = BeautifulSoup(responce.text, 'html.parser')

books = html_soup.find_all('div', class_="book-info")

nowe = set()


for b in books:
    nowe.add(b.a.text)


# jeśli get sobie nie radzi to korzystamy z SELENIUM
# inna możliwość to scrapy

