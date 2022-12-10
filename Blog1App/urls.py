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
    
    path('',views.mostrar_index,  name='Home'),
    path('mostrar_alimentacion/', views.mostrar_alimentacion, name='Alimentacion'),
    path('hacer_ejercicio/', views.Hacer_ejercicio, name='Musculacion'),
    path('consejo_antistress/',views.Consejo_antistress, name='Relax'),
    path('buscar_ejercicio/',views.buscar_ejercicio, name='Buscar Ejercicio'),
    path('buscar_dieta/',views.buscar_dieta, name='Buscar Dieta'),
    path('buscar_relax/',views.buscar_relax, name='Buscador relax'),
    path('mostrar_ejercicio/',views.mostrar_ejercicio, name='Mostrar Ejercicios'),
    path('eliminar_ejercicio/<ejercicio_id>',views.eliminar_ejercicio, name='Eliminar Ejercicio'),
    path('modificar_ejercicio/<ejercicio_id>',views.Modificar_ejercicio, name='Modificar Ejercicio'),
    path('mostrar_relax/',views.mostrar_relax, name='Mostrar Relax'),
    path('eliminar_relax/<relax_id>',views.eliminar_relax, name='Eliminar Relax'),
    path('Modificar_antistress/<relax_id>',views.Modificar_antistress, name='Modificar Relax'),
    path('mostrar_dieta/',views.mostrar_comida,name='Mostrar Alimentacion'),
    path('eliminar_alimentacion/<alimentacion_id>',views.eliminar_alimentacion,name='Eliminar Alimentacion'),
    path('Modificar_alimentacion/<alimentacion_id>',views.Modificar_alimentacion,name='Modificar Alimentacion'),
    path('signup/',views.SignUpView.as_view(),name='signup'),
    path('login/', views.AdminLoginView.as_view(), name='Login'),
    path('logout/', views.AdminLogoutView.as_view(), name='Logout'),
    path('mostrar_contacto',views.mostrar_contacto,  name='Contacto'),
    path('mostrar_terminos',views.mostrar_terminos,  name='Terminos'),
    path('modificar_usuario/', views.modificar_usuario, name='Modificar Usuario')
    
    
]








