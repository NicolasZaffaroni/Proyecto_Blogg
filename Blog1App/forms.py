from django import forms



class Dieta_form(forms.Form):
    Desayuno= forms.CharField()
    Almuerzo = forms.CharField()
    Merienda = forms.CharField()
    Cena = forms.CharField()
    