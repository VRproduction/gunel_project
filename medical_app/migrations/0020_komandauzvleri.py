# Generated by Django 3.2.7 on 2021-09-17 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medical_app', '0019_komandayazi'),
    ]

    operations = [
        migrations.CreateModel(
            name='Komandauzvleri',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sekil', models.ImageField(upload_to='media/')),
                ('adsoyad', models.CharField(max_length=20)),
                ('vezife', models.CharField(max_length=15)),
            ],
        ),
    ]
