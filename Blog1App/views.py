
from django.shortcuts import render
from .models import Alimentacion , Movibilidad
from django.http import HttpResponse

# Create your views here.
def Hacer_Movilidad(request):
    #Movibilidad = Movibilidad(Ejercicio='Saludo al sol', Musculo_Implicado='Espalda baja')
    movibilidad =  Movibilidad(Ejercicio="Saludo al sol", Musculo_Implicado="Espalda Baja")

    elongar =f"El ejercicio que haremos es hoy {movibilidad.Ejercicio}, los musculos que trabajan y estiran son {movibilidad.Musculo_Implicado}"
    return HttpResponse(elongar)



def mostrar_index(request):

    return render(request,"index.html")



def mostrar_alimentacion(request):

    return render(request , 'Alimentacion.html')


def Hacer_ejercicio(request):

    return render(request ,"Ejercicios.html")


def Crear_plato(request):
    if request.method == "Plato":


        plato_ideal = plato_ideal(Proteina =request.Plato["Proteina"],Hidrato =request.Plato["Hidrato"],Fibra= request.Plato["Fibra"] )

        plato_ideal.save(Alimentacion)        

        return render(request,"index.html")


    return render(request ,"crear_alimento.html")
# Create your views here.
