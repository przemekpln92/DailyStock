from django.conf import settings
import re
from django.shortcuts import redirect

"""class LoginRequiredMiddleware:

	def __init__(self, get_response):
		self.get_response = get_response

	def __call__(self, request):
		response = self.get_response(request)
		return response

	def process_view(self, request, view_func, view_args, view_kwargs):
		if True:
			return redirect(settings.LOGIN_URL)"""