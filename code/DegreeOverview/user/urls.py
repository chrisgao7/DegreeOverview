from django.contrib import admin
from django.http.request import validate_host
from django.urls import path, include
from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),

    path('cdMain', views.cdMain, name='cdMain'),
    path('ncdMain', views.ncdMain, name='ncdMain'),
    path('stuMain', views.stuMain, name='stuMain'),

    path('home', views.home, name='home')
]
