from django.shortcuts import render

# Create your views here.

def inicio(request):
	return render(request,'comprar/index.html')

def coleccion(request):
	return render(request,'inicio/coleccion.html')