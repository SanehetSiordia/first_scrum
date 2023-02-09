from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import usuario
from .forms import UsuarioForm
# Create your views here.

def inicio(request):
    return render(request, 'pages/inicio.html')

def registros(request):
    registros=usuario.objects.all()
    return render(request, 'registros/index.html',{'usuarios':registros})

def crear(request):
    formulario=UsuarioForm(request.POST or None,request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('registros')
    return render(request, 'registros/crear.html',{'formulario':formulario})
    
def editar(request, id):
    registro=usuario.objects.get(id=id)
    formulario=UsuarioForm(request.POST or None,request.FILES or None,instance=registro)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('registros')
    return render(request, 'registros/editar.html',{'formulario':formulario})

def eliminar(request, id):
    registro=usuario.objects.get(id=id)
    registro.delete()
    return redirect('registros')
    


