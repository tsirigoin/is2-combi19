# Generated by Django 3.2 on 2021-04-26 19:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='chofer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('correo', models.CharField(max_length=200)),
                ('informacion_contacto', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='combi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patente', models.CharField(max_length=20)),
                ('tipo', models.CharField(max_length=100)),
                ('capacidad', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(999)])),
            ],
        ),
    ]
