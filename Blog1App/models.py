from django.db import models

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

    Proteina = models.CharField(max_length=40)
    Hidratos = models.CharField(max_length=40)
    Fibra = models.CharField(max_length=40)
