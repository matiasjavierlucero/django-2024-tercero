# Generated by Django 4.2.11 on 2024-08-16 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_productimage_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
