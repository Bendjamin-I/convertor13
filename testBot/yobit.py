import requests


def get_btc():
	url = 'https://yobit.net/api/2/btc_usd/ticker'
	response = requests.get(url).json()
	prise = response['ticker']['last']
	return str(int(prise)) + ' usd'
	
print(get_btc())
