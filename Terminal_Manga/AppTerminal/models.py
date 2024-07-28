from django.db import models

class Mangas(models.Model):
    Anime = models.CharField(max_length=40)
    Arco = models.IntegerField()

class Usuarios(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)

class Vendedores(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)
    apellido = models.CharField(max_length=30)

