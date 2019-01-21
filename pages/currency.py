from forex_python.converter import CurrencyRates
from datetime import datetime

def usd_rates():
	c = CurrencyRates()
	today = datetime.now()
	usdrates= c.get_rates('USD',today)
	return usdrates