from django.db import models
from django.contrib.auth.models import User

# Create your models here.from django.db import models

# Create your models here.
class Movibilidad(models.Model):

    Ejercicio = models.CharField(max_length=40)
    Musculo_Implicado = models.CharField(max_length=40)


class Velocidad(models.Model):

    Ejercicio = models.CharField(max_length=40)
    Metros= models.CharField(max_length=40)
    Tiempo= models.IntegerField(max_length=40)


class Pesas(models.Model):

    Ejercicio = models.CharField(max_length=40)
    Musculo_Implicado  = models.CharField(max_length=40)
    Descanso = models.CharField(max_length=40)
    


class Alimentacion(models.Model):

    Proteina= models.CharField(max_length=40)
    Hidratos= models.CharField(max_length=40)
    Fibra= models.CharField(max_length=40)



class Antistress(models.Model):

    Ejercicio = models.CharField(max_length=40)
    Descanso = models.CharField(max_length=40)
    Terreno_Recomendado= models.CharField(max_length=200, null=True)
    Link_Musica = models.CharField(max_length=200, null=True)
    Link_Video = models.CharField(max_length=200, null=True)






class Musculacion(models.Model):

    Ejercicio = models.CharField(max_length=40)
    Musculo_Implicado  = models.CharField(max_length=40)
    Carga = models.CharField(max_length=40)
    Series= models.CharField(max_length=40, null=True)
    Descanso = models.CharField(max_length=40)
    Nivel = models.CharField(max_length=40, null=True)
    Link_Video = models.CharField(max_length=200, null=True)



class Avatar(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    imagen = models.ImageField(upload_to='images/', null=True, blank=True)

