from django.shortcuts import render, render_to_response, redirect
from django.conf import settings
from pages.forms import (
	TickerAndDate, 
	RegistrationForm, 
	EditProfileForm,
	CurrencyForm
)
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
import datetime
from pandas_datareader import data, get_nasdaq_symbols
import pandas as pd
from bokeh.plotting import figure, show, output_file
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.embed import components
from bokeh.resources import CDN
from django.contrib.auth.models import User
import requests
from IPython.display import HTML
from forex_python.converter import CurrencyCodes


#Common variables
error = "Wrong format or date range! Remember, data is available only 5 years back"
error_two = "Wrong ticker! Complete list of tickers you can finde here: https://iextrading.com/trading/eligible-symbols/"



#Home page
def index(request):

	if not request.user.is_authenticated:
		return redirect( 'login')

	from .plots import candle_stick
	from .methods import ticker_date_get,post, start_date_converter, percentage
	from .indices import dia, spy, iwm, jpxn
	from .currency import usd_rates

	#Ticker and date form
	ticker_date_form = ticker_date_get(TickerAndDate())
	

	#Indices bar
	dia = dia()
	dia_close = dia[0]
	dia_percentage = round(percentage(dia[0],dia[1]),3)
	spy = spy()
	spy_close = spy[0]
	spy_percentage = round(percentage(spy[0],spy[1]),3)
	iwm = iwm()
	iwm_close = iwm[0]
	iwm_percentage = round(percentage(iwm[0],iwm[1]),3)
	jpxn = jpxn()
	jpxn_close = jpxn[0]
	jpxn_percentage = round(percentage(jpxn[0],jpxn[1]),3)

	#Currency
	usdrates = usd_rates()

	#News
	source = 'https://newsapi.org/v2/top-headlines?sources=financial-post&apiKey=ea7db87a666841fcaffa98a85e706f7c'
	json = requests.get(source).json()
	request.session['jsonnews'] = json

	try:
		if request.method == "POST":
			text = TickerAndDate(request.POST)
			if text.is_valid():
				ticker = text.cleaned_data['ticker']
				date = text.cleaned_data['date']
				ticker_choice = request.session['tickerpost'] = ticker
				date_choice = request.session['datepost'] = date

				start_date = start_date_converter(date_choice)
				candle_stick = candle_stick(ticker_choice, start_date)

				request.session['plot'] = candle_stick[1]
				request.session['plotjs'] = candle_stick[2]
				request.session['plotcss'] = candle_stick[3]
				request.session['plotscript'] = candle_stick[0]
				
			return render( request,'index.html',{
				'ticker_date_form':ticker_date_form, 
				"ticker":ticker,
				"dia_close":dia[0],
				"dia_prev_close":dia[1],
				"dia_name":dia[2][1][:14],
				"dia_percentage":dia_percentage,
				"spy_close":spy[0],
				"spy_prev_close":spy[1],
				"spy_name":spy[2][1],
				"spy_percentage":spy_percentage,
				"iwm_close":iwm[0],
				"iwm_prev_close":iwm[1],
				"iwm_name":iwm[2][1],
				"iwm_percentage":iwm_percentage,
				"jpxn_close":jpxn_close,
				"jpxn_prev_close":jpxn[1],
				"jpxn_name":jpxn[2][1],
				"jpxn_percentage":jpxn_percentage,
				"aud":usdrates["AUD"],
				"eur":usdrates["EUR"],
				"gbp":usdrates["GBP"],
				"chf":usdrates["CHF"],
				"dkk":usdrates["DKK"],
				"nok":usdrates["NOK"],
				"sek":usdrates["SEK"],
				"rub":usdrates["RUB"],
				"pln":usdrates["PLN"],
				'json':json,
				})
		else:
			return render( request,'index.html',{
				'ticker_date_form':ticker_date_form, 
				"dia_close":dia[0],
				"dia_prev_close":dia[1],
				"dia_name":dia[2][1][:14],
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
				"aud":usdrates["AUD"],
				"eur":usdrates["EUR"],
				"gbp":usdrates["GBP"],
				"chf":usdrates["CHF"],
				"dkk":usdrates["DKK"],
				"nok":usdrates["NOK"],
				"sek":usdrates["SEK"],
				"rub":usdrates["RUB"],
				"pln":usdrates["PLN"],
				'json':json,
				})
	except KeyError:
		return render( request,'index.html',{
			'ticker_date_form':ticker_date_form, 
			"text":text, 
			"error":error_two,
			"dia_close":dia[0],
			"dia_prev_close":dia[1],
			"dia_name":dia[2][1][:14],
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
			"aud":usdrates["AUD"],
			"eur":usdrates["EUR"],
			"gbp":usdrates["GBP"],
			"chf":usdrates["CHF"],
			"dkk":usdrates["DKK"],
			"nok":usdrates["NOK"],
			"sek":usdrates["SEK"],
			"rub":usdrates["RUB"],
			"pln":usdrates["PLN"],
			'json':json,
			})
	except ValueError:
		return render( request,'index.html',{
			'ticker_date_form':ticker_date_form, 
			"text":text, 
			"error":error,
			"dia_close":dia[0],
			"dia_prev_close":dia[1],
			"dia_name":dia[2][1][:14],
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
			"aud":usdrates["AUD"],
			"eur":usdrates["EUR"],
			"gbp":usdrates["GBP"],
			"chf":usdrates["CHF"],
			"dkk":usdrates["DKK"],
			"nok":usdrates["NOK"],
			"sek":usdrates["SEK"],
			"rub":usdrates["RUB"],
			"pln":usdrates["PLN"],
			'json':json,
			})


#Charts page
def charts(request):
	from .plots import candle_stick, one_line, volume
	from .methods import ticker_date_get,post, start_date_converter

	if not request.user.is_authenticated:
		return redirect( 'login')

	#Ticker and date form
	ticker_date_form = ticker_date_get(TickerAndDate())
	try:
		if request.method == 'POST':
			text = TickerAndDate(request.POST)
			if text.is_valid():
				ticker = text.cleaned_data['ticker']
				date = text.cleaned_data['date']
				ticker_choice = request.session['tickerpost'] = ticker
				date_choice = request.session['datepost'] = date

				start_date = start_date_converter(date_choice)
				candle_stick = candle_stick(ticker_choice, start_date)
				close_price = one_line(ticker_choice, start_date)
				volume = volume(ticker_choice, start_date)

				#Sessions
				request.session['chplot'] = candle_stick[1]
				request.session['chplotjs'] = candle_stick[2]
				request.session['chplotcss'] = candle_stick[3]
				request.session['chplotscript'] = candle_stick[0]

				request.session['plotclose'] = close_price[1]
				request.session['plotjsclose'] = close_price[2]
				request.session['plotcssclose'] = close_price[3]
				request.session['plotscriptclose'] = close_price[0]

				request.session['plotvolume'] = volume[1]
				request.session['plotjsvolume'] = volume[2]
				request.session['plotcssvolume'] = volume[3]
				request.session['plotscriptvolume'] = volume[0]


			return render(request,"charts.html",{
				'ticker_date_form':ticker_date_form,
				"text":text,
				"js":candle_stick[2],
				"css":candle_stick[3],
				"script":candle_stick[0],
				"div":candle_stick[1],
				"js_close":close_price[2],
				"css_close":close_price[3],
				"script_close":close_price[0],
				"div_close":close_price[1],
				"js_volume":volume[2],
				"css_volume":volume[3],
				"script_volume":volume[0],
				"div_volume":volume[1],

			})

		else:
			return render(request,"charts.html",{
				'ticker_date_form':ticker_date_form,})

	except KeyError:
		return render(request,"charts.html",{
				'ticker_date_form':ticker_date_form,
				'error':error_two,
				})
	except ValueError:
		return render(request,"charts.html",{
				'ticker_date_form':ticker_date_form,
				'error':error,
				})


#Tables page
def tables(request):

	from .methods import ticker_date_get,post, start_date_converter, table_generator
	from .plots import get_security_name

	if not request.user.is_authenticated:
		return redirect( 'login')

	#Ticker and date form
	ticker_date_form = ticker_date_get(TickerAndDate())

	
	try:
		if request.method == "POST":
			text = TickerAndDate(request.POST)
			if text.is_valid():
				ticker = text.cleaned_data['ticker']
				date = text.cleaned_data['date']
				ticker_choice = request.session['tickerposttable'] = ticker
				date_choice = request.session['datepost'] = date
				security_name = get_security_name(ticker)
				request.session['security_name'] = security_name[1]

				#Table generation
				start_date = start_date_converter(date_choice)
				table_generator = table_generator(ticker_choice, start_date)

				#Sessions
				request.session['table_generator'] = table_generator

			return render(request,"tables.html",{
				'ticker_date_form':ticker_date_form,
			})

		else:
			return render(request,"tables.html",{
				'ticker_date_form':ticker_date_form,})
	except KeyError:
		return render(request,"tables.html",{
				'ticker_date_form':ticker_date_form,
				'error':error_two,
				})
	except ValueError:
		return render(request,"tables.html",{
				'ticker_date_form':ticker_date_form,
				'error':error,
				})

def rates(request):
	from .currency import all_rates

	if not request.user.is_authenticated:
		return redirect( 'login')

	currency_form = CurrencyForm()

	if request.method == "POST":
		text = CurrencyForm(request.POST)
		if text.is_valid():
			currency_choice = text.cleaned_data['currency']
			all_rates = all_rates(currency_choice)
			c = CurrencyCodes()
			name = c.get_currency_name(currency_choice)
			curr=[]
			values = []

			for item in all_rates:
			    curr.append(item)

			for value in all_rates.values():
			    values.append(value)

			for x in curr:
				frame = {'Symbol' : curr,'Rates' : values}
				df = pd.DataFrame(frame)
				table = df.to_html(classes = 'table table-striped table-bordered table-hover', index=False)

			request.session['table'] = table
			request.session['name'] = name

			return render(request,"rates.html",{
					'currency_choice':currency_choice,
					'currency_form':currency_form,
					})
	else:
		return render(request,"rates.html",{
			'currency_form':currency_form,
			})





def datasource(request):
	if not request.user.is_authenticated:
		return redirect( 'login')
		
	return render(request,"datasource.html",{})


@login_required
def logout(request):
	return render(request,"registration/logout.html",{})


def register(request):
	if request.method == "POST":
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/index')
	else:
		form = RegistrationForm()

		args = {"form": form}
		return render (request,'registration/register.html', args)


@login_required
def profile(request):
	args = {'user':request.user}
	return render(request,"registration/profile.html",args)


@login_required
def edit_profile(request):
	if request.method == 'POST':
		form = EditProfileForm(request.POST, instance=request.user)

		if form.is_valid():
			form.save()
			return redirect('profile')

	else:
		form = EditProfileForm(instance=request.user)
		args = {'form': form}
		return render(request,'registration/edit_profile.html',args)


@login_required
def change_password(request):
	if request.method == 'POST':
		form = PasswordChangeForm(data=request.POST, user=request.user)

		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)
			return redirect('profile')
		else:
			return redirect('change_password')

	else:
		form = PasswordChangeForm(user=request.user)
		args = {'form': form}
		return render(request,'registration/change_password.html',args)