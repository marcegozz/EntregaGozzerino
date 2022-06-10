from django.shortcuts import render
from django.http import HttpResponse
from Aplicacion.forms import nuevoAvistamiento, nuevaOrganización, nuevoHeroe
from Aplicacion.models import Superhumano, Avistamiento, Organizacion

def inicio(request):
    return render(request, "-")

def nuevoAvistamiento(request):
    if request.method == 'POST':
        miFormulario = NuevaAparicion(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            aparicion = Aparicion(descripcionLugar = informacion['descripcionLugar'], superhumano=informacion['superhumano'])
            aparicion.save()
            return render(request, "-")
    else:
            miFormulario = NuevaAparicion()
    return render(request, "-", {"miFormulario":miFormulario})

def nuevoHeroe(request):
    if request.method == 'POST':
        miFormulario = NuevoHeroe(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            heroe = Superhumano(nombre = informacion['nombre'], nivelDePoder=informacion['poder'])
            heroe.save()
            return render(request, "-")
    else:
            miFormulario = NuevoHeroe()
    return render(request, "-", {"miFormulario":miFormulario})

def nuevaOrganizacion(request):
    if request.method == 'POST':
        miFormulario = NuevaOrganizacion(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            organizacion = Organizacion(nombre = informacion['nombre'], cantIntegrantes=informacion['cantIntegrantes'])
            organizacion.save()
            return render(request, "-")
    else:
            miFormulario = NuevaOrganizacion()
    return render(request, "-", {"miFormulario":miFormulario})

def buscarAparicion(request):
    return render(request, "-")

def buscar(request):
    if request.GET["superhumano"]:
        heroe = request.GET["superhumano"]
        apariciones = Aparicion.objects.filter(superhumano__icontains=heroe)
        return render(request, "-", {"superhumano":heroe,"apariciones":apariciones})
    else:
        respuesta = "No enviaste datos"
        return HttpResponse(respuesta)


