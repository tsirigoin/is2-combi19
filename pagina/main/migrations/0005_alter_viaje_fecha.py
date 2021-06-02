# Generated by Django 3.2.3 on 2021-06-02 19:04

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_combi_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='viaje',
            name='fecha',
            field=models.DateField(validators=[django.core.validators.MinValueValidator(datetime.date(2021, 6, 3))]),
        ),
    ]
