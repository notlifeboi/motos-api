# Generated by Django 5.0.7 on 2024-07-27 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motos_api', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moto',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
