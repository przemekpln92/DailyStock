from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout

urlpatterns = [
    path('',LoginView.as_view(), name='login'),
    path('index/',views.index, name='index'),
    path('charts/',views.charts, name='charts'),
    path('tables/',views.tables, name='tables'),
    path('datasource/',views.datasource, name='datasource'),
    path('login/', LoginView.as_view(), name='login'),
    path('registration/logout/',views.logout, name='logout'),
    path('registration/register/',views.register, name='register'),
    path('registration/profile/',views.profile, name='profile'),
    path('registration/edit_profile/',views.edit_profile, name='edit_profile'),
]