from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views #Para que no haya conflicto con las views normales
from . import views 

urlpatterns = [
    path('login/',auth_views.LoginView.as_view(),name="login"), #vista de login
    path('logout/',auth_views.LogoutView.as_view(), name="logout"), #vista de logout
    path('enter/',include("apps.comprar.urls")),
    path('registrate/',views.registrate, name="registrate"),
]