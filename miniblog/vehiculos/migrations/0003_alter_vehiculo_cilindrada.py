# Generated by Django 5.0.6 on 2024-07-04 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculos', '0002_vehiculo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiculo',
            name='cilindrada',
            field=models.FloatField(),
        ),
    ]
