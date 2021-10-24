from django import forms
from django.forms import fields, widgets
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post

class Formulario_registro_usuario(UserCreationForm):
    username = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")
    email = forms.EmailField(label="Correo")
    password1 = forms.CharField(label="Contraseña",widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir Contraseña",widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username','last_name','email','password1','password2']
        help_texts = {k:"" for k in fields}

class PostForm(forms.ModelForm):
    contenido = forms.CharField(label='',widget=forms.Textarea(attrs={'rows':2,'placeholder':'hola'}),required=True)

    class Meta:
        model=Post
        fields=['contenido']