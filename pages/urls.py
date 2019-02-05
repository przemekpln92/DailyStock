from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth.views import LoginView, LogoutView
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
    path('logout/',auth_views.LogoutView.as_view(template_name="registration/logout.html"), name='logout'),
    path('registration/register/',views.register, name='register'),
    path('registration/profile/',views.profile, name='profile'),
    path('registration/edit_profile/',views.edit_profile, name='edit_profile'),
    path('registration/password/',views.change_password, name='change_password'),
    path('registration/reset_password',
        auth_views.PasswordResetView.as_view(template_name="registration/reset_password.html"),
        name="reset_password"),
    path('password_reset/done/',
        auth_views.PasswordResetDoneView.as_view(template_name="registration/reset_password_done.html"),
        name="reset_password_done"),
    path('reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(template_name="registration/reset_password_confirm.html"),
        name="reset_password_confirm"),
    path('reset/done/',
        auth_views.PasswordResetView.as_view(template_name="registration/reset_password_complete.html"),
        name="reset_password_complete"),

]