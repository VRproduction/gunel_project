# Generated by Django 3.2.7 on 2021-09-19 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medical_app', '0041_auto_20210919_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='melumatsektoru',
            name='boyuk_yazi',
            field=models.CharField(help_text='Maksimum 30 simvol', max_length=30),
        ),
        migrations.AlterField(
            model_name='melumatsektoru',
            name='kicik_yazi',
            field=models.CharField(help_text='Maksimum 50 simvol', max_length=50),
        ),
    ]
