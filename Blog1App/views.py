
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


            pesas= Musculacion(Ejercicio=formulario_limpio['Ejercicio'],Musculo_Implicado=formulario_limpio['Musculo_Implicado'],Carga=formulario_limpio['Carga'],Series=formulario_limpio['Series'],Descanso=formulario_limpio['Descanso'],Nivel=formulario_limpio['Nivel'],Link_Video=formulario_limpio['Link_Video'])

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






def mostrar_ejercicio(request):
    entrenamiento = Musculacion.objects.all()

    context = {'entrenamiento':entrenamiento}

    return render(request,'mostrar_ejercicio.html', context=context )





def eliminar_ejercicio(request, ejercicio_id):
    entrenamiento_eliminado = Musculacion.objects.get(id = ejercicio_id )

    entrenamiento_eliminado.delete()


    entrenamiento = Musculacion.objects.all()

    context = {'entrenamiento':entrenamiento}

    return render(request,'mostrar_ejercicio.html', context=context )






def Modificar_ejercicio(request,ejercicio_id):

    pesas = Musculacion.objects.get(id = ejercicio_id )

    if request.method == "POST":
        formulario= Musculacion_form(request.POST)

        if formulario.is_valid():

            formulario_limpio = formulario.cleaned_data


            pesas.Ejercicio=formulario_limpio['Ejercicio']
            pesas.Musculo_Implicado=formulario_limpio['Musculo_Implicado']
            pesas.Carga=formulario_limpio['Carga']
            pesas.Series=formulario_limpio['Series']
            pesas.Descanso=formulario_limpio['Descanso']
            pesas.Nivel=formulario_limpio['Nivel']
            pesas.Link_Video=formulario_limpio['Link_Video']
            
            pesas.save()

            return render(request,'index.html')


    else:
        formulario= Musculacion_form(initial={'Ejercicio':pesas.Ejercicio,'Musculo_Implicado':pesas.Musculo_Implicado,'Carga':pesas.Carga,'Series':pesas.Series,'Descanso':pesas.Descanso,'Nivel':pesas.Nivel,'Link_Video':pesas.Link_Video})




    return render(request ,"modificar_ejercicio.html",{'formulario':formulario})









def mostrar_relax(request):
    relajate= Antistress.objects.all()

    context = {'relajate':relajate}

    return render(request,'mostrar_relax.html', context=context )




def eliminar_relax(request, relax_id):
    relax_eliminado = Antistress.objects.get(id = relax_id )

    relax_eliminado.delete()


    relajate= Antistress.objects.all()

    context = {'relajate':relajate}

    return render(request,'mostrar_relax.html', context=context )





def Modificar_antistress(request,relax_id):

    consejos_relax= Antistress.objects.get(id = relax_id )
    
    if request.method == "POST":
        formulario= Antistress_form(request.POST)

        if formulario.is_valid():
            formulario_limpio = formulario.cleaned_data

            consejos_relax.Ejercicio=formulario_limpio['Ejercicio']
            consejos_relax.Descanso=formulario_limpio['Descanso']
            consejos_relax.Terreno_Recomendado=formulario_limpio['Terreno_Recomendado']
            consejos_relax.Link_Musica=formulario_limpio['Link_Musica']
            consejos_relax.Link_Video=formulario_limpio['Link_Video']


            consejos_relax.save()

            return render(request, 'index.html')

    else:
        formulario= Antistress_form(initial={'Ejercicio':consejos_relax.Ejercicio,'Descanso':consejos_relax.Descanso,'Terreno_Recomendado':consejos_relax.Terreno_Recomendado,'Link_Musica':consejos_relax.Link_Musica,'Link_Video':consejos_relax.Link_Video})




    return render(request ,"modifica_relax.html" ,{'formulario':formulario})