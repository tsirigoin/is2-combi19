# Generated by Django 3.2.3 on 2021-06-08 22:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0001_initial'),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='viaje',
            name='chofer',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='users.chofer'),
        ),
        migrations.AddField(
            model_name='viaje',
            name='combi',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='main.combi'),
        ),
        migrations.AddField(
            model_name='viaje',
            name='comentarios',
            field=models.ManyToManyField(blank=True, to='main.Comentario'),
        ),
        migrations.AddField(
            model_name='viaje',
            name='insumo',
            field=models.ManyToManyField(blank=True, to='main.Insumo'),
        ),
        migrations.AddField(
            model_name='viaje',
            name='pasajeros',
            field=models.ManyToManyField(blank=True, to='main.Pasajero'),
        ),
        migrations.AddField(
            model_name='viaje',
            name='ruta',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='main.ruta'),
        ),
        migrations.AddField(
            model_name='ruta',
            name='destino',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='destino', to='main.lugar'),
        ),
        migrations.AddField(
            model_name='ruta',
            name='origen',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='origen', to='main.lugar'),
        ),
        migrations.AddField(
            model_name='pasajero',
            name='usuario',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='lugar',
            unique_together={('localidad', 'provincia')},
        ),
        migrations.AddField(
            model_name='comentario',
            name='usuario',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='viaje',
            unique_together={('chofer', 'fecha', 'hora', 'ruta')},
        ),
        migrations.AlterUniqueTogether(
            name='ruta',
            unique_together={('origen', 'destino')},
        ),
    ]