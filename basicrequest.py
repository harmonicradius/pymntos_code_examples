import requests
from bs4 import BeautifulSoup

search_term = 'PyMNtos'
url = 'https://www.google.com/search?q={}'.format(search_term)
html_doc = requests.get(url)

soup = BeautifulSoup(html_doc.text, "html.parser")

links = []
for item in soup.find_all('h3', attrs={'class' : 'r'}):
    print item.text
    print '\t'+item.a['href'][7:]  # [7:] strips the /url?q= prefix
