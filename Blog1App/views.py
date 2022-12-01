
from django.shortcuts import render
from .models import Alimentacion, Musculacion,Antistress
from django.http import HttpResponse
from .forms import Alimentacion_form,Musculacion_form,Antistress_form

# Create your views here.
def Hacer_Movilidad(request):
    #Movibilidad = Movibilidad(Ejercicio='Saludo al sol', Musculo_Implicado='Espalda baja')
    movibilidad =  movibilidad(Ejercicio="Saludo al sol", Musculo_Implicado="Espalda Baja")

    elongar =f"El ejercicio que haremos es hoy {movibilidad.Ejercicio}, los musculos que trabajan y estiran son {movibilidad.Musculo_Implicado}"
    return HttpResponse(elongar)



def mostrar_index(request):

    return render(request,"index.html")



def mostrar_alimentacion(request):
    if request.method == "POST":


        formulario= Alimentacion_form(request.POST)

        if formulario.is_valid():

            formulario_limpio = formulario.cleaned_data


            alimentacion = Alimentacion(Proteina=formulario_limpio['Proteina'],Hidratos=formulario_limpio['Hidratos'],Fibra=formulario_limpio['Fibra'])


            alimentacion.save()

            return render(request, 'index.html')

    else:
        formulario= Alimentacion_form()


    return render(request , 'Alimentacion.html',{'formulario':formulario})


def Hacer_ejercicio(request):
    if request.method == "POST":
        formulario= Musculacion_form(request.POST)

        if formulario.is_valid():

            formulario_limpio = formulario.cleaned_data


            pesas= Musculacion(Ejercicio=formulario_limpio['Ejercicio'],Musculo_Implicado=formulario_limpio['Musculo_Implicado'],Carga=formulario_limpio['Carga'],Descanso=formulario_limpio['Descanso'],Nivel=formulario_limpio['Nivel'],Link_Video=formulario_limpio['Link_Video'])

            pesas.save()

            return render(request,'index.html')


    else:
        formulario= Musculacion_form()




    return render(request ,"Ejercicios.html",{'formulario':formulario})







# Create your views here.



def Consejo_antistress(request):
    if request.method == "POST":
        formulario= Antistress_form(request.POST)

        if formulario.is_valid():
            formulario_limpio = formulario.cleaned_data

            consejos_relax= Antistress(Ejercicio=formulario_limpio['Ejercicio'],Descanso=formulario_limpio['Descanso'],Terreno_Recomendado=formulario_limpio['Terreno_Recomendado'],Link_Musica=formulario_limpio['Link_Musica'],Link_Video=formulario_limpio['Link_Video'])

            consejos_relax.save()

            return render(request, 'index.html')

    else:
        formulario= Antistress_form()



    return render(request ,"Antistress.html" ,{'formulario':formulario})






def buscar_ejercicio(request):
    if request.GET.get('Ejercicio',False ):
        Ejercicio= request.GET['Ejercicio']
        Musculos = Musculacion.objects.filter(Ejercicio__icontains=Ejercicio)

        return render(request,'buscar_ejercicio.html',{"Musculos":Musculos})
    else:
        respuesta= 'No hay ejercicios cargados,anda al apartado Musculacion y carga el tuyo!'
    return render(request,"buscar_ejercicio.html",{'respuesta': respuesta })








def buscar_dieta(request):
    if request.GET.get('Proteina',False ):
        Proteina= request.GET['Proteina']
        Dieta= Alimentacion.objects.filter(Proteina__icontains=Proteina)

        return render(request,'buscar_dieta.html',{"Dieta":Dieta})
    else:
        respuesta= 'No se encontro el plato, que buscas, carga el tuyo en la seccion Alimento, asi otros usuarios pueden verlo'
    return render(request,"buscar_dieta.html",{'respuesta': respuesta })
    





    



def buscar_relax(request):
    if request.GET.get('Ejercicio',False ):
        Ejercicio= request.GET['Ejercicio']
        Relajate= Antistress.objects.filter(Ejercicio__icontains=Ejercicio)

        return render(request,'buscar_relax.html',{"Relajate":Relajate})
    else:
        respuesta= 'No se encontro el ejercicio , que buscas, carga el tuyo en la seccion Relajarte, asi otros usuarios pueden verlo'
    return render(request,"buscar_relax.html",{'respuesta': respuesta })





