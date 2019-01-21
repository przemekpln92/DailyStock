from django.shortcuts import render, render_to_response
from pages.forms import TickerAndDate, TickerForm
import datetime
from pandas_datareader import data, get_nasdaq_symbols
import pandas as pd
from bokeh.plotting import figure, show, output_file
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.embed import components
from bokeh.resources import CDN

# Create your views here.



def index(request):
	from .plots import candle_stick
	from .methods import ticker_date_get,post, start_date_converter, percentage
	from .indices import dia, spy, iwm, jpxn
	from .currency import usd_rates

	#Ticker and date form
	ticker_date_form = ticker_date_get(TickerAndDate())
	text = post(TickerAndDate(request.POST))

	#Indices bar
	dia = dia()
	dia_percentage = round(percentage(dia[0],dia[1]),3)
	spy = spy()
	spy_percentage = round(percentage(spy[0],spy[1]),3)
	iwm = iwm()
	iwm_percentage = round(percentage(iwm[0],iwm[1]),3)
	jpxn = jpxn()
	jpxn_percentage = round(percentage(jpxn[0],jpxn[1]),3)

	#Currency
	usdrates = usd_rates()


	try:
		if type(text) == tuple:
			start_date = start_date_converter(text[1])
			candle_stick = candle_stick(text[0], start_date)
			return render( request,'index.html',{
				"js":candle_stick[2],
				"css":candle_stick[3],
				"script":candle_stick[0],
				"div":candle_stick[1],
				'ticker_date_form':ticker_date_form, 
				"text":text,
				"dia_close":dia[0],
				"dia_prev_close":dia[1],
				"dia_name":dia[2][1],
				"dia_percentage":dia_percentage,
				"spy_close":spy[0],
				"spy_prev_close":spy[1],
				"spy_name":spy[2][1],
				"spy_percentage":spy_percentage,
				"iwm_close":iwm[0],
				"iwm_prev_close":iwm[1],
				"iwm_name":iwm[2][1],
				"iwm_percentage":iwm_percentage,
				"jpxn_close":jpxn[0],
				"jpxn_prev_close":jpxn[1],
				"jpxn_name":jpxn[2][1],
				"jpxn_percentage":jpxn_percentage,
				"aud":usdrates["AUD"]
				})
		else:
			return render( request,'index.html',{
				'ticker_date_form':ticker_date_form, 
				"text":text,
				"dia_close":dia[0],
				"dia_prev_close":dia[1],
				"dia_name":dia[2][1],
				"dia_percentage":dia_percentage,
				"spy_close":spy[0],
				"spy_prev_close":spy[1],
				"spy_name":spy[2][1],
				"spy_percentage":spy_percentage,
				"iwm_close":iwm[0],
				"iwm_prev_close":iwm[1],
				"iwm_name":iwm[2][1],
				"iwm_percentage":iwm_percentage,
				"jpxn_close":jpxn[0],
				"jpxn_prev_close":jpxn[1],
				"jpxn_name":jpxn[2][1],
				"jpxn_percentage":jpxn_percentage,
				"aud":usdrates["AUD"]
				})
	except KeyError:
		error = "Wrong ticker! Complete list of tickers you can finde here: https://iextrading.com/trading/eligible-symbols/"
		return render( request,'index.html',{
			'ticker_date_form':ticker_date_form, 
			"text":text, 
			"error":error,
			"dia_close":dia[0],
			"dia_prev_close":dia[1],
			"dia_name":dia[2][1],
			"dia_percentage":dia_percentage,
			"spy_close":spy[0],
			"spy_prev_close":spy[1],
			"spy_name":spy[2][1],
			"spy_percentage":spy_percentage,
			"iwm_close":iwm[0],
			"iwm_prev_close":iwm[1],
			"iwm_name":iwm[2][1],
			"iwm_percentage":iwm_percentage,
			"jpxn_close":jpxn[0],
			"jpxn_prev_close":jpxn[1],
			"jpxn_name":jpxn[2][1],
			"jpxn_percentage":jpxn_percentage,
			"aud":usdrates["AUD"]
			})
	except ValueError:
		error = "Wrong format or date range! Remember, data is available only 5 years back"
		return render( request,'index.html',{
			'ticker_date_form':ticker_date_form, 
			"text":text, 
			"error":error,
			"dia_close":dia[0],
			"dia_prev_close":dia[1],
			"dia_name":dia[2][1],
			"dia_percentage":dia_percentage,
			"spy_close":spy[0],
			"spy_prev_close":spy[1],
			"spy_name":spy[2][1],
			"spy_percentage":spy_percentage,
			"iwm_close":iwm[0],
			"iwm_prev_close":iwm[1],
			"iwm_name":iwm[2][1],
			"iwm_percentage":iwm_percentage,
			"jpxn_close":jpxn[0],
			"jpxn_prev_close":jpxn[1],
			"jpxn_name":jpxn[2][1],
			"jpxn_percentage":jpxn_percentage,
			"aud":usdrates["AUD"]
			})

def charts(request):
	return render(request,"charts.html",{})

def tables(request):
	return render(request,"tables.html",{})

def datasource(request):
	return render(request,"datasource.html",{})

def forms(request):
	def get():
		form = HomeForm()
		return form
	form = get()
	def post():
		form = HomeForm(request.POST)
		if form.is_valid():
			text = form.cleaned_data['post']
			return text

	text = post()

	args = {'form':form, "text":text }


	return render(request,"forms.html",args)