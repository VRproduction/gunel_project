# Generated by Django 3.2.15 on 2022-12-16 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_app', '0009_mobileəsasfoto'),
    ]

    operations = [
        migrations.CreateModel(
            name='SEO_Əlaqə',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('metatag', models.TextField()),
            ],
        ),
    ]
