# Generated by Django 3.2.7 on 2021-09-17 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medical_app', '0014_auto_20210917_1302'),
    ]

    operations = [
        migrations.CreateModel(
            name='HaqqimizdaYazilar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yazi_1', models.CharField(max_length=50)),
                ('yazi_2', models.CharField(max_length=50)),
                ('yazi_3', models.CharField(max_length=60)),
                ('yazi_4', models.CharField(max_length=50)),
            ],
        ),
    ]
