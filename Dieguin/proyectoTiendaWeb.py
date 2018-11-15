"""
Estas son las funciones que utilizan las view del proyecto de Django, la tienda de relojes. Leer atentamente para el correcto funcionamiento.
"""

def registrate(request):
	"""
	Esta función recibe una solicitud y nos ayuda a registrar nuevos usuarios.
	Se debe ubicar en el archivo apps/clientes/views.py
	Es importante hacer los siguientes imports:
	from django.shortcuts import render, redirect
	from django.contrib.auth.forms import UserCreationForm
	from django.contrib.auth import authenticate,login,logout
	from django.contrib.auth.decorators import login_required
	from .forms import UserCreateForm
	"""
	if request.method == 'POST':
		form = UserCreateForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username,password=password)
			login(request,user)
			return redirect('inicio2')
	else:
		form = UserCreateForm()
	return render(request,'registration/registrate.html',{'form':form})

def inicio(request):
	"""
	Esta función sirve para volver a la página de inicio, e igualmente recibe una petición.
	Su ubicación es el archivo: apps/comprar/views.py
	También debe estar presente en: apps/inicio/views.py
	Para su correcto funcionamiento, se requiere importar:
	from django.shortcuts import render
	"""
	return render(request,'comprar/index.html')

def coleccion(request):
	"""
	Esta función sirve para navegar a la página de colección, e igualmente recibe una petición.
	Su ubicación es el archivo: apps/comprar/views.py
	También debe estar presente en: apps/inicio/views.py

	Para su correcto funcionamiento, se requiere importar:
	from django.shortcuts import render
	"""
	return render(request,'inicio/coleccion.html')
