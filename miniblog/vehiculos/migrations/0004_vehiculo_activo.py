# Generated by Django 5.0.6 on 2024-08-15 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculos', '0003_alter_vehiculo_cilindrada'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehiculo',
            name='activo',
            field=models.BooleanField(default=True),
        ),
    ]
