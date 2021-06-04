# Generated by Django 3.2 on 2021-06-02 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20210602_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='combi',
            name='tipo',
            field=models.CharField(choices=[('super comoda', 'Super Comoda'), ('comoda', 'Comoda')], max_length=12),
        ),
        migrations.AlterField(
            model_name='pasajero',
            name='estado',
            field=models.CharField(choices=[('finalizado', 'Finalizado'), ('viajando', 'Viajando'), ('reservado', 'Reservado')], max_length=12),
        ),
    ]