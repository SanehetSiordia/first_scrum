from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def inicio(request):
    return HttpResponse('<h1>Bienvenido a la pagina de inicio<h1>')

