from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
	path('',views.inicio,name='inicio'),
	path('colecciones/',views.coleccion,name='colecciones'),
]
