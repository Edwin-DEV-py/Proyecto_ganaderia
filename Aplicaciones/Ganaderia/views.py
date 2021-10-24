from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import Formulario_registro_usuario, PostForm
from .models import *
from .forms import Formulario_registro_usuario
from django.contrib import messages

def inicio(request):
    return render(request,'index.html')

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
    current_user = get_object_or_404(User, pk=request.user.pk)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
            messages.success(request, 'Post hecho')
            return redirect('index.html')
    else:
        form = PostForm()
    return render(request,'post.html',{'form':form})
# Create your views here.
