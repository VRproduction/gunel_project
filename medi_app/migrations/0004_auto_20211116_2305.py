# Generated by Django 3.2.7 on 2021-11-16 23:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medi_app', '0003_rename_müsahibə_müsahibe'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MediaTvProqramları',
        ),
        migrations.DeleteModel(
            name='MediaYouTube',
        ),
        migrations.DeleteModel(
            name='Müsahibe',
        ),
    ]
