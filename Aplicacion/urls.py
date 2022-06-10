from django.urls import URLPattern, path
from Aplicacion import views

URLPattern = [
    path('', views.inicio, name="index"),
    path('nuevoAvistamiento', views.nuevoAvistamiento, name = "nuevaAparicion"),
    path('buscarAvistamiento', views.buscarAvistamiento, name = "buscarAparicion"),
    path('nuevoHeroe', views.nuevoHeroe, name = "nuevoHeroe"),
    path('nuevaOrganizacion', views.nuevaOrganizacion, name = "nuevaOrganizacion"),
    path('buscar/', views.buscar)
]