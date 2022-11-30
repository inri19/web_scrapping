import requests
from bs4 import BeautifulSoup as soup

url = 'https://coinmarketcap.com/'
page_doc = requests.get(url).content

ma_soupe = soup(page_doc, 'html.parser')

tbody = ma_soupe.find('tbody')
trs = tbody.find_all('tr')

for i, tr in enumerate(trs[:10]) :

	# NOM DE LA CRYPTO
	nom = tr.contents[2].find_all('p')[0].string 
	
	# PRIX DE LA CRYPTO
	prix = tr.contents[3].find('span').string

	# MARKET CAP
	market_cap = tr.contents[7].find_all('span')[1].string
	
	# MONNAIE EN CIRCULATION
	crypto_circ = tr.contents[9].find('p').string

	if i == 0 :

		print('\n')
		print('----------------------------------------------------------------------')
		print('\n')

	print(f'Position : {i+1}')
	print(f'Nom : {nom}')
	print(f'Prix : {prix}')
	print(f'Market Cap : {market_cap}')
	print(f'Monnaie en circulation : {crypto_circ}')

	print('\n')
	print('----------------------------------------------------------------------')
	print('\n')
	
# print(tbody.prettify())