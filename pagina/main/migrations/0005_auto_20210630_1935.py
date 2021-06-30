# Generated by Django 3.2 on 2021-06-30 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20210630_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pasajero',
            name='estado',
            field=models.CharField(choices=[('reservado', 'Reservado'), ('cancelado', 'Cancelado'), ('finalizado', 'Finalizado'), ('perdido', 'Perdido'), ('viajando', 'Viajando')], default='reservado', max_length=12),
        ),
        migrations.AlterField(
            model_name='test',
            name='estado',
            field=models.CharField(choices=[('positivo', 'Positivo'), ('negativo', 'Negativo')], max_length=12),
        ),
        migrations.AlterField(
            model_name='viaje',
            name='estado',
            field=models.CharField(choices=[('finalizado', 'Finalizado'), ('reservado', 'Reservado'), ('viajando', 'Viajando'), ('cancelado', 'Cancelado')], default='reservado', max_length=12),
        ),
    ]