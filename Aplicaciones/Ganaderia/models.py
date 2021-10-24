from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import resolve_url
from django.utils import timezone


class Perfil(models.Model):
    nombre = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Perfil de {self.nombre.username}'


class Post(models.Model):
    nombre = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    tiempo_publicacion = models.DateTimeField(default=timezone.now)
    contenido = models.TextField()

    class Meta:
        ordering = ['-tiempo_publicacion']

    def __str__(self):
        return f'{self.nombre.username}:{self.contenido}'
# Create your models here.
