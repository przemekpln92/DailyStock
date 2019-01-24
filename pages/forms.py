from django import forms
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

#Ticker and date from from home page
class TickerAndDate(forms.ModelForm):
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
			'placeholder': 'From(yyyy-mm-dd)',
			'style':'display: inline-block;max-width: 150px;margin-right:20px;margin-top:10px'
			}
		),label="")
	class Meta:
		model = Post
		fields = ("ticker","date",)

#Registration form
class RegistrationForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = (
			'username',
			'first_name',
			'last_name',
			'email',
			'password1',
			'password2'
		)

	def save(self, commit=True):
		user = super(RegistrationForm, self).save(commit=False)
		user.first_name = self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['last_name']
		user.email = self.cleaned_data['email']

		if commit:
			user.save()

		return user


class EditProfileForm(UserChangeForm):

	class Meta:
		model = User
		fields = (
			'email',
			'first_name',
			'last_name',
			'password'
		)

