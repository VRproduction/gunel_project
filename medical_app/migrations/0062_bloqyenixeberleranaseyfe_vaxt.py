# Generated by Django 3.2.7 on 2021-09-20 10:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('medical_app', '0061_bloqyenixeberleranaseyfe_tarix'),
    ]

    operations = [
        migrations.AddField(
            model_name='bloqyenixeberleranaseyfe',
            name='vaxt',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
    ]
