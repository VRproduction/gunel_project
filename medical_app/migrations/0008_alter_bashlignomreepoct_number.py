# Generated by Django 3.2.7 on 2021-09-17 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medical_app', '0007_rename_numberemail_bashlignomreepoct'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bashlignomreepoct',
            name='number',
            field=models.IntegerField(max_length=50),
        ),
    ]
