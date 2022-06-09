from django.db import models

class Superhumano (models.Model):
        nombre = models.CharField(max_length=40)
        edad = models.IntegerField()

class Organizacion(models.Model):
    nombre = models.CharField(max_length=40)
    cantIntegrantes = models.IntegerField()

class Avistamiento(models.Model):
    superhumano = models.CharField(max_length=40)
    descripcionLugar = models.CharField(max_length=100)
    
