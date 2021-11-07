# Generated by Django 3.2.7 on 2021-09-20 10:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('medical_app', '0062_bloqyenixeberleranaseyfe_vaxt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bloqyenixeberleranaseyfe',
            name='vaxt',
        ),
        migrations.AlterField(
            model_name='bloqyenixeberleranaseyfe',
            name='tarix',
            field=models.DateField(default=django.utils.timezone.now, help_text='Avtomatik ozü vaxtı təyin edəcək'),
        ),
    ]
