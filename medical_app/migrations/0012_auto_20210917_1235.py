# Generated by Django 3.2.7 on 2021-09-17 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medical_app', '0011_auto_20210917_1233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slayderyazilar',
            name='yazi_1',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='slayderyazilar',
            name='yazi_3',
            field=models.CharField(max_length=100),
        ),
    ]
