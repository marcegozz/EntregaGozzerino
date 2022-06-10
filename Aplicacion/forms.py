from django import forms

class nuevoAvistamiento(forms.form):
    descripcionLugar = forms.CharField()
    superHumano = forms.CharField()

class nuevoHeroe(forms.form):
    nombre = forms.CharField()

class nuevaOrganización(forms.form):
    nombre = forms.CharField()
    cantIntegrantes = forms.IntegerField()

    