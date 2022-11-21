from django import forms



class Alimentacion_form(forms.Form):
    Proteina= forms.CharField()
    Hidratos= forms.CharField()
    Fibra= forms.CharField()







class Musculacion_form(forms.Form):
    Ejercicio= forms.CharField(max_length=40)
    Musculo_Implicado = forms.CharField(max_length=40)
    Carga= forms.CharField()
    Descanso= forms.CharField(max_length=40)
    Nivel = forms.CharField( )
    Link_Video = forms.CharField( )




class Antistress_form(forms.Form):

    Ejercicio =forms.CharField(max_length=40)
    Descanso = forms.CharField()
    Terreno_Recomendado= forms.CharField(max_length=200, )
    Link_Musica = forms.CharField(max_length=200, )
    Link_Video = forms.CharField(max_length=200, )