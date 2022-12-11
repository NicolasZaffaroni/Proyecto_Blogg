from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class Alimentacion_form(forms.Form):
    Proteina= forms.CharField()
    Hidratos= forms.CharField()
    Fibra= forms.CharField()







class Musculacion_form(forms.Form):
    Ejercicio= forms.CharField(max_length=40)
    Musculo_Implicado = forms.CharField(max_length=40)
    Carga= forms.CharField()
    Series= forms.CharField(max_length=40,)
    Descanso= forms.CharField(max_length=40)
    Nivel = forms.CharField( )
    Link_Video = forms.CharField( )




class Antistress_form(forms.Form):

    Ejercicio =forms.CharField(max_length=40)
    Descanso = forms.CharField()
    Terreno_Recomendado= forms.CharField(max_length=200, )
    Link_Musica = forms.CharField(max_length=200, )
    Link_Video = forms.CharField(max_length=200, )





class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]





class UserEditForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]
        help_texts = {k: '' for k in fields}






#class Avatar(UserEditForm):


    #User= forms.ForeignKey(User, on_delete=forms.CASCADE)

    #imagen = forms.ImageField(upload_to='images/', null=True, blank=True)
