# Generated by Django 3.2.7 on 2021-09-23 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qebul_app', '0006_qəbul_form_arxa_foto'),
    ]

    operations = [
        migrations.CreateModel(
            name='QəbulXəritə',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('xerite_url', models.TextField(help_text='Google Xəritənin Linki', max_length=250)),
            ],
        ),
    ]
