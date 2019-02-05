from datetime import datetime, timedelta
from .models import Post
from pandas_datareader import data
from pandas import DataFrame
import datetime
from IPython.display import HTML
import os
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

#Table generator
def table_generator(ticker,start_date):

	start = datetime.datetime(start_date[0],start_date[1],start_date[2])

	df = data.DataReader(name=ticker, data_source="iex", start=start, end=None)
	
	#Saving dataframe as an csv file
	file_dir = os.path.dirname(os.path.abspath(__file__))
	csv_folder = 'static/csv'
	file_path = os.path.join(file_dir, csv_folder, 'data.csv')
	df.to_csv(file_path, header=True, index=True)
	df = df.reset_index().rename(columns={'date':'date'})
	df['index'] = df.index
	df.set_index('index')

	for x in df.index:
	    frame = {'Date' : df['date'],
	    		'Open' : df['open'],
	    		'High' : df['high'],
	            'Low' : df['low'],
	            'Close' : df['close'],
	            }
	df = DataFrame(frame)
	html = df.to_html(classes = 'table table-striped table-bordered table-hover', table_id='dataTables-example', index=False)

	return html