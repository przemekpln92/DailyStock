from datetime import datetime, timedelta
from .models import Post

#Get/post ticker and date form
def ticker_date_get(TickerAndDate):
	ticker_date_form = TickerAndDate
	return ticker_date_form

def post(request,PostTickerAndDate):
	form = PostTickerAndDate
	if form.is_valid():
		post = form.save(commit=False)
		post.user = request.user
		post.save()
		text = form.cleaned_data['ticker']
		text_two = form.cleaned_data['date']
		return text, text_two

#Date converter
def start_date_converter(date):
    start_date = date
    x = start_date.split('-')
    result = list(map(int, x))
    return result
#Percentage converter
def percentage(close, prev_close):
  return 100 * float(close)/float(prev_close) - 100