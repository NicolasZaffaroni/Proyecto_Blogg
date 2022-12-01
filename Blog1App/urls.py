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
from Blog1App import  views
urlpatterns =[
    
    path('',views.mostrar_index),
    path('mostrar_alimentacion/', views.mostrar_alimentacion, name='Alimentacion'),
    path('hacer_ejercicio/', views.Hacer_ejercicio, name='Musculacion'),
    path('consejo_antistress/',views.Consejo_antistress, name='Relax'),
    path('buscar_ejercicio/',views.buscar_ejercicio, name='Buscar Ejercicio'),
    path('buscar_dieta/',views.buscar_dieta, name='Buscar Dieta'),
    path('buscar_relax/',views.buscar_relax, name='Buscador relax')
    
]








