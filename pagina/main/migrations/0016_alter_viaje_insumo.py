# Generated by Django 3.2 on 2021-05-12 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_alter_viaje_insumo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='viaje',
            name='insumo',
            field=models.ManyToManyField(blank=True, to='main.Insumo'),
        ),
    ]
