# Generated by Django 3.2.7 on 2021-10-18 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medical_app', '0086_remove_haqqımızdayazılar_yazi_1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='haqqımızdamüəllif',
            name='adsoyad',
            field=models.CharField(help_text='Maksimum 50 hərif', max_length=50),
        ),
        migrations.AlterField(
            model_name='haqqımızdamüəllif',
            name='vezife',
            field=models.CharField(help_text='Maksimum 30 hərif', max_length=30),
        ),
    ]
