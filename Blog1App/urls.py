"""ProyectoCoder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import Hacer_Movilidad , mostrar_index, mostrar_alimentacion, Hacer_ejercicio,Crear_plato

urlpatterns =[
    path("Hacer_Movilidad/",Hacer_Movilidad),
    path('', mostrar_index),
    path('mostrar_alimentacion/', mostrar_alimentacion, name='Alimentacion'),
    path('hacer_ejercicio/',Hacer_ejercicio, name='Ejercicio'),
    path('Crear_plato/',Crear_plato, name='Crear Plato')
]








