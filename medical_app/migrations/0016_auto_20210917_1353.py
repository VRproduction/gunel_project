# Generated by Django 3.2.7 on 2021-09-17 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medical_app', '0015_haqqimizdayazilar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='haqqimizdayazilar',
            name='yazi_1',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='haqqimizdayazilar',
            name='yazi_2',
            field=models.CharField(max_length=35),
        ),
    ]
