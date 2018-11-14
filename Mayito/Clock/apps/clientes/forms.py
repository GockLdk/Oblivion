"""
El documento forms de esta app (clientes) se encarga de definir la form de clientes. 
"""

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):
	"""
	Esta clase recibe como parámetro UserCreationForm, y de ella extrae model y fields, donde va a recibir el nombre de usuario y las contraseñas.
	"""
	class Meta: #De la clase UserCreationForm solo jalare
		model = User
		fields = ("username","password1","password2")