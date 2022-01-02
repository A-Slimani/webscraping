from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup

html = urlopen('https://gg.deals')
bs = BeautifulSoup(html.read(), 'lxml')

