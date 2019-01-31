from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.index, name='index'),
    path('index/',views.index, name='index'),
    path('charts/',views.charts, name='charts'),
    path('tables/',views.tables, name='tables'),
    path('rates/',views.rates, name='rates'),
    path('datasource/',views.datasource, name='datasource'),
    path('login/', LoginView.as_view(), name='login'),
    path('registration/logout/',views.logout, name='logout'),
    path('registration/register/',views.register, name='register'),
    path('registration/profile/',views.profile, name='profile'),
    path('registration/edit_profile/',views.edit_profile, name='edit_profile'),
    path('registration/change_password/',views.change_password, name='change_password'),
    path('registration/reset_password', auth_views.PasswordResetView.as_view(), name="reset_password"),
    path('registration/reset_password_done', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('registration/reset_password_confirm', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('registration/reset_password_complete', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),

]