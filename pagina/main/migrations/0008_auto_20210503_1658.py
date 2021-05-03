# Generated by Django 3.2 on 2021-05-03 19:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='ruta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origen', models.CharField(max_length=100)),
                ('destino', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='viaje',
            name='lugar_llegada',
        ),
        migrations.RemoveField(
            model_name='viaje',
            name='lugar_salida',
        ),
        migrations.AddField(
            model_name='viaje',
            name='ruta',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='main.ruta'),
        ),
    ]
