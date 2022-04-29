from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import Formulario_registro_usuario, PostForm, PublicacionForm
from .models import *
from .forms import Formulario_registro_usuario
from django.contrib import messages

def inicio(request):
    publicaciones = Publicacion.objects.all()
    contexto = {'publicaciones':publicaciones}
    data = {
        'publicaciones':Publicacion.objects.all()
    }
    return render(request,'index.html',contexto)

def categorias(request):
    return render(request,'categorias.html')

def seccion(request):
    return render(request, 'seccion.html')

def iniciar_seccion(request):
    return render(request,'iniciar_seccion.html')
    
def registrarse(request):
    if request.method == 'POST':
        form = Formulario_registro_usuario(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request,f'Usuario {username} creado')
            return redirect('index.html')
    else:
        form = Formulario_registro_usuario()
    contexto = {'form':form}
    return render(request,'registrarse.html',contexto)

def perfil(request):
    return render(request,'perfil.html')

def post(request):
    if request.method == 'GET':
        form = PublicacionForm()
        contexto = {'form':form}
    else:
        form = PublicacionForm(request.POST)
        contexto = {'form':form}
    if form.is_valid():
        form.save()
        messages.success(request, 'Post hecho')
        return redirect('index.html')
    return render(request,'post.html',contexto)
# Create your views here.
