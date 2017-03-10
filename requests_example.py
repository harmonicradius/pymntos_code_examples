import requests
import json
from bs4 import BeautifulSoup

search_term = 'Jeskai Ascendancy'
#search_term = sys.argv[1]
scgurl = 'http://sales.starcitygames.com/search.php?substring='+search_term
html_doc = requests.get(scgurl)

soup = BeautifulSoup(html_doc.text, "html.parser")


tdlist= soup.findAll('td')
result = {}
item={}



for ted in tdlist:
	if ted.get('class') != None:
		if str(ted.get('class')[0]) == 'deckdbbody2' or str(ted.get('class')[0]) == 'deckdbbody':  #the blueones
			if str(ted.get('class')[1]) == 'search_results_1':
				if ted.find('a') != None:
					card_name = ted.find('a').text.replace('\n','')

			if str(ted.get('class')[1]) == 'search_results_2':
				if ted.find('a') != None:
					card_set =  ted.find('a').text

			if str(ted.get('class')[1]) == 'search_results_6':
				rarity = ted.text

			if str(ted.get('class')[1]) == 'search_results_7':
				condition = ted.text

			if str(ted.get('class')[1]) == 'search_results_9':
					bigdivlist =  ted.findAll('div')
					for smalldiv in bigdivlist:
						divlist = smalldiv.findAll('div')
						if divlist != []:
							print card_name, card_set, '\n\t',
							print divlist