from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('index/',views.index, name='index'),
    path('charts/',views.charts, name='charts'),
    path('tables/',views.tables, name='tables'),
    path('datasource/',views.datasource, name='datasource'),
]