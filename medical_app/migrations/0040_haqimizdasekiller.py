# Generated by Django 3.2.7 on 2021-09-19 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medical_app', '0039_delete_haqimizdasekiller'),
    ]

    operations = [
        migrations.CreateModel(
            name='HaqimizdaSekiller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('esas_sekil', models.ImageField(help_text='Fotonu olcuye uygun yukleyin...', upload_to='media/')),
                ('orta_sekil', models.ImageField(help_text='Kicik foto yukluyun...', upload_to='media/')),
            ],
        ),
    ]
