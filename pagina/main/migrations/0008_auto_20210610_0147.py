# Generated by Django 3.2 on 2021-06-10 04:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20210610_0040'),
    ]

    operations = [
        migrations.AddField(
            model_name='pasajero',
            name='dni',
            field=models.CharField(default=None, max_length=10, validators=[django.core.validators.MinLengthValidator(6)]),
        ),
        migrations.AlterField(
            model_name='combi',
            name='tipo',
            field=models.CharField(choices=[('super comoda', 'Super Comoda'), ('comoda', 'Comoda')], max_length=12),
        ),
        migrations.AlterField(
            model_name='pasajero',
            name='estado',
            field=models.CharField(choices=[('viajando', 'Viajando'), ('reservado', 'Reservado'), ('finalizado', 'Finalizado')], max_length=12),
        ),
    ]
