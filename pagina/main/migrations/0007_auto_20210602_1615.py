# Generated by Django 3.2 on 2021-06-02 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20210602_1613'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comentario',
            name='fecha',
        ),
        migrations.AlterField(
            model_name='combi',
            name='tipo',
            field=models.CharField(choices=[('super comoda', 'Super Comoda'), ('comoda', 'Comoda')], max_length=12),
        ),
    ]
