# Generated by Django 4.1.3 on 2022-11-14 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alimentacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Proteina', models.CharField(max_length=40)),
                ('Hidratos', models.CharField(max_length=40)),
                ('Fibra', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Movibilidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ejercicio', models.CharField(max_length=40)),
                ('Musculo_Implicado', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Pesas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ejercicio', models.CharField(max_length=40)),
                ('Musculo_Implicado', models.CharField(max_length=40)),
                ('Descanso', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Velocidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ejercicio', models.CharField(max_length=40)),
                ('Metros', models.CharField(max_length=40)),
                ('Tiempo', models.IntegerField(max_length=40)),
            ],
        ),
    ]