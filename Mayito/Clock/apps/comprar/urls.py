from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
	path('inicio/',views.inicio,name='inicio2'),
	path('colecciones/',views.coleccion,name='colecciones'),
]