# Generated by Django 3.2 on 2021-05-13 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210513_1045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='combi',
            name='tipo',
            field=models.CharField(choices=[('super comoda', 'Super Comoda'), ('comoda', 'Comoda')], max_length=12),
        ),
    ]
