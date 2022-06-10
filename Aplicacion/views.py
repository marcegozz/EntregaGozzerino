from django.shortcuts import render
from django.http import HttpResponse
from Aplicacion.forms import nuevoAvistamiento, nuevaOrganización, nuevoHeroe
from Aplicacion.models import Superhumano, Avistamiento, Organizacion

def inicio(request):
    return render(request, "Aplicacion/index.html")

def nuevoAvistamiento(request):
    if request.method == 'POST':
        miFormulario = nuevoAvistamiento(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            aparicion = Avistamiento(descripcionLugar = informacion['descripcionLugar'], superhumano=informacion['superhumano'])
            aparicion.save()
            return render(request, "Aplicacion/index.html")
    else:
            miFormulario = nuevoAvistamiento()
    return render(request, "Alicacion/nuevoAvistamiento.html", {"miFormulario":miFormulario})

def nuevoHeroe(request):
    if request.method == 'POST':
        miFormulario = nuevoHeroe(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            heroe = Superhumano(nombre = informacion['nombre'], nivelDePoder=informacion['poder'])
            heroe.save()
            return render(request, "Aplicacion/index.html")
    else:
            miFormulario = nuevoHeroe()
    return render(request, "Aplicacion/nuevoHeroe.html", {"miFormulario":miFormulario})

def nuevaOrganizacion(request):
    if request.method == 'POST':
        miFormulario = nuevaOrganizacion(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            organizacion = Organizacion(nombre = informacion['nombre'], cantIntegrantes=informacion['cantIntegrantes'])
            organizacion.save()
            return render(request, "Aplicacion/index.html")
    else:
            miFormulario = nuevaOrganizacion()
    return render(request, "Aplicacion/index.html", {"miFormulario":miFormulario})

def buscarAvistamiento(request):
    return render(request, "Aplicacion/buscarAvistamiento.html")

def buscar(request):
    if request.GET["superhumano"]:
        heroe = request.GET["superhumano"]
        apariciones = Avistamiento.objects.filter(superhumano__icontains=heroe)
        return render(request, "Aplicacion/resultadoBusquedaAvistamiento.html", {"superhumano":heroe,"apariciones":apariciones})
    else:
        respuesta = "No enviaste datos"
        return HttpResponse(respuesta)


