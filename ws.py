from urllib.request import urlopen
from urllib.error import HTTPError, URLError 
from bs4 import BeautifulSoup

html = urlopen('https://gg.deals/games/tekken-7/')
bs = BeautifulSoup(html.read(), 'lxml')

# test to see if it detects the webpage
# if bs == None:
# 	print("---EMPTY---")
# else:
# 	print(bs)

# collect links from webpage
for link in bs.find_all('a'):
	if 'href' in link.attrs:
		print(link.attrs['href'])
