# Generated by Django 3.2.7 on 2021-11-29 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medical_app', '0094_rename_foto_mobilefoto_foto_res'),
    ]

    operations = [
        migrations.CreateModel(
            name='SEO_AnaSəhifə',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('metatag', models.TextField()),
            ],
        ),
    ]
