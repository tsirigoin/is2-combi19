# Generated by Django 3.2 on 2021-05-11 14:05

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20210510_2044'),
    ]

    operations = [
        migrations.AddField(
            model_name='viaje',
            name='hora',
            field=models.TimeField(default=None),
        ),
        migrations.AddField(
            model_name='viaje',
            name='precio',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=10, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='combi',
            name='patente',
            field=models.CharField(max_length=10, unique=True, validators=[django.core.validators.MinLengthValidator(6)]),
        ),
        migrations.AlterField(
            model_name='combi',
            name='tipo',
            field=models.CharField(choices=[('mediano', 'Mediano'), ('chico', 'Chico'), ('grande', 'Grande')], max_length=10),
        ),
        migrations.AlterField(
            model_name='insumo',
            name='precio',
            field=models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='viaje',
            name='fecha',
            field=models.DateField(validators=[django.core.validators.MinValueValidator(datetime.date(2021, 5, 12))]),
        ),
        migrations.RemoveField(
            model_name='viaje',
            name='insumo',
        ),
        migrations.AddField(
            model_name='viaje',
            name='insumo',
            field=models.ManyToManyField(blank=True, to='main.Insumo'),
        ),
    ]
