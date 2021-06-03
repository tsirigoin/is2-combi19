# Generated by Django 3.2 on 2021-06-02 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20210602_1618'),
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
            field=models.CharField(choices=[('viajando', 'Viajando'), ('reservado', 'Reservado'), ('finalizado', 'Finalizado')], max_length=12),
        ),
    ]
