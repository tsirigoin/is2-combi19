# Generated by Django 3.2.3 on 2021-06-08 22:30

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Combi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patente', models.CharField(max_length=10, unique=True, validators=[django.core.validators.MinLengthValidator(6)])),
                ('tipo', models.CharField(choices=[('super comoda', 'Super Comoda'), ('comoda', 'Comoda')], max_length=12)),
                ('capacidad', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(999)])),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Insumo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True)),
                ('descripcion', models.CharField(max_length=100)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0)])),
                ('cantidad', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(999)])),
            ],
        ),
        migrations.CreateModel(
            name='Lugar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('localidad', models.CharField(max_length=150)),
                ('provincia', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Pasajero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(choices=[('reservado', 'Reservado'), ('finalizado', 'Finalizado'), ('viajando', 'Viajando')], max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Ruta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Viaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=100)),
                ('fecha', models.DateField(validators=[django.core.validators.MinValueValidator(datetime.date(2021, 6, 9))])),
                ('hora', models.TimeField(default=None)),
                ('precio', models.DecimalField(decimal_places=2, default=None, max_digits=10, validators=[django.core.validators.MinValueValidator(0)])),
            ],
        ),
    ]