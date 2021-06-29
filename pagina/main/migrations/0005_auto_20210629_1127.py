# Generated by Django 3.2.4 on 2021-06-29 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20210629_1116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='combi',
            name='tipo',
            field=models.CharField(choices=[('comoda', 'Comoda'), ('super comoda', 'Super Comoda')], max_length=12),
        ),
        migrations.AlterField(
            model_name='pasajero',
            name='estado',
            field=models.CharField(choices=[('cancelado', 'Cancelado'), ('viajando', 'Viajando'), ('reservado', 'Reservado'), ('finalizado', 'Finalizado')], default='reservado', max_length=12),
        ),
        migrations.AlterField(
            model_name='viaje',
            name='estado',
            field=models.CharField(choices=[('cancelado', 'Cancelado'), ('viajando', 'Viajando'), ('reservado', 'Reservado'), ('finalizado', 'Finalizado')], default='reservado', max_length=12),
        ),
    ]
