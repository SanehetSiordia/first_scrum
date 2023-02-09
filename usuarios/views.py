from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import usuario
from .forms import UsuarioForm
# Create your views here.

def inicio(request):
    return render(request, 'pages/inicio.html')


def registros(request):
    registros=usuario.objects.all()    
    print(type(registros))
    print(registros)
    print(registros[0].nombre)
    print(registros[0].numero)
    print(registros[0].apellido)
    print(registros[0].edad)
    return render(request, 'registros/index.html',{'usuarios':registros})

def crear(request):
    formulario=UsuarioForm(request.POST or None,request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('registros')
    return render(request, 'registros/crear.html',{'formulario':formulario})
    
def editar(request):
    return render(request, 'registros/editar.html')
    


