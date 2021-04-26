# Generated by Django 3.2 on 2021-04-26 20:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210426_1755'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chofer',
            name='viaje',
        ),
        migrations.RemoveField(
            model_name='combi',
            name='viaje',
        ),
        migrations.RemoveField(
            model_name='insumo',
            name='viaje',
        ),
        migrations.AddField(
            model_name='viaje',
            name='chofer',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='main.chofer'),
        ),
        migrations.AddField(
            model_name='viaje',
            name='combi',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='main.combi'),
        ),
        migrations.AlterField(
            model_name='viaje',
            name='fecha',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='viaje',
            name='lugar_salida',
            field=models.CharField(max_length=100),
        ),
    ]