
from django.shortcuts import render
from .models import Alimentacion , Movibilidad
from django.http import HttpResponse
from .forms import Dieta_form

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
    if request.method == "POST":


        alimentacion = Alimentacion( Proteína=request.POST["Proteína"],Hidrato=request.POST["Hidrato"],Fibra=request.POST["Fibra"] )

        alimentacion.save(Alimentacion)        

        return render(request,"index.html")




    return render(request ,"crear_alimento.html")
# Create your views here.
