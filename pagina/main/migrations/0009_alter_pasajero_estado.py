# Generated by Django 3.2 on 2021-06-10 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20210610_0147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pasajero',
            name='estado',
            field=models.CharField(choices=[('viajando', 'Viajando'), ('finalizado', 'Finalizado'), ('reservado', 'Reservado')], max_length=12),
        ),
    ]
