from forex_python.converter import CurrencyRates
from datetime import datetime

def usd_rates():
	c = CurrencyRates()
	usdrates= c.get_rates('USD')
	return usdrates

def all_rates(currency):
	c = CurrencyRates()
	rates= c.get_rates(currency)
	return rates