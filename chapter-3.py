from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('https://gg.deals')
bs = BeautifulSoup(html, 'lxml')
for link in bs.find_all('a'):
	if 'href' in link.attrs:
		print(link.attrs['href'])