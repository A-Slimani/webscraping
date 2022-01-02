from urllib.request import urlopen
from bs4 import BeautifulSoup

bs = BeautifulSoup(html.read(), 'html.parser')


html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')

# find all based of html tag
# find_all(tag, attributes, recursive, text, limit, keywords)
nameList = bs.findAll('span', {'class':'green'})

# find - gets the first of that instance
title = bs.find(id='title')

html2 = urlopen('http://www.pythonscraping.com/pages/page3.html')

# getting descendant tag
for child in bs.find('table',{'id':'giftlist'}).children:
	print(child) # could add this val to an array or dictionary

# using regex for bs4
import re
images = bs.find_all('img', {'src':re.compile('\.\.\/img\/gifts/img.*\.jpg')})
for image in images:
	print(image['src'])
