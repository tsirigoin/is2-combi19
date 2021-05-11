# Generated by Django 3.2.2 on 2021-05-10 23:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_chofer'),
        ('main', '0010_auto_20210510_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='viaje',
            name='chofer',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='users.chofer'),
        ),
        migrations.DeleteModel(
            name='chofer',
        ),
    ]
