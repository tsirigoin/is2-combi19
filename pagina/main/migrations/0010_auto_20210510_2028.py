# Generated by Django 3.2.2 on 2021-05-10 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20210503_1722'),
    ]

    operations = [
        migrations.DeleteModel(
            name='usuario',
        ),
        migrations.AlterField(
            model_name='combi',
            name='patente',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='insumo',
            name='nombre',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='ruta',
            name='destino',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='ruta',
            name='origen',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterUniqueTogether(
            name='lugar',
            unique_together={('localidad', 'provincia')},
        ),
        migrations.AlterUniqueTogether(
            name='ruta',
            unique_together={('origen', 'destino')},
        ),
        migrations.AlterUniqueTogether(
            name='viaje',
            unique_together={('chofer', 'fecha', 'ruta')},
        ),
    ]