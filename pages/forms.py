from django import forms

class TickerAndDate(forms.Form):
	ticker = forms.CharField(widget=forms.TextInput(
			attrs={
			'class': 'form-control',
			'placeholder': 'Ticker',
			}
		),label="")
	date = forms.CharField(widget=forms.TextInput(
			attrs={
			'class': 'form-control',
			'placeholder': 'yyyy-mm-dd'
			}
		),label="")
	
class TickerForm(forms.Form):
	ticker = forms.CharField(widget=forms.TextInput(
			attrs={
			'class': 'form-control',
			'placeholder': 'Ticker',
			}
		),label="")