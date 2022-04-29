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

lista_animales = [
    ('Abeja','Abeja'),
    ('Caballo','Caballo'),
    ('Cabra','Cabra'),
    ('Cerdo','Cerdo'),
    ('Conejo','Conejo'),
    ('Gallina','Gallina'),
    ('Gallo','Gallo'),
    ('Obeja','Obeja'),
    ('Pato','Pato'),
    ('pez','pez'),
    ('Toro','Toro'),
    ('Vaca','Vaca')
]

lista_sexo = [
    (1,'Macho'),
    (2,'Hembra')
]

class Publicacion(models.Model):
    id = models.AutoField(primary_key=True)
    animal = models.CharField(
        max_length=10,
        choices=lista_animales,
        default="Animal"
    )
    Anos = models.CharField(max_length=2)
    Sexo = models.IntegerField(
        null = False, blank=False,
        choices=lista_sexo,
        default="Genero"
    )
    image = models.ImageField(null=True, blank=True)
    def __str__(self):
        return self
# Create your models here.
