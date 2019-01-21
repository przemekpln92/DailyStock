from django import forms

class TickerAndDate(forms.Form):
	ticker = forms.CharField(widget=forms.TextInput(
			attrs={
			'class': 'form-control',
			'placeholder': 'Ticker',
			'style':'display: inline-block; max-width: 150px; vertical-align: top;margin-right:20px;margin-top:10px'
			}
		),label="")
	date = forms.CharField(widget=forms.TextInput(
			attrs={
			'class': 'form-control',
			'placeholder': 'yyyy-mm-dd',
			'style':'display: inline-block;max-width: 150px;margin-right:20px;margin-top:10px'
			}
		),label="")
	
class TickerForm(forms.Form):
	ticker = forms.CharField(widget=forms.TextInput(
			attrs={
			'class': 'form-control',
			'placeholder': 'Ticker',
			}
		),label="")