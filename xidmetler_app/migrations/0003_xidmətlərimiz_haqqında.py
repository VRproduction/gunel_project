# Generated by Django 3.2.7 on 2021-10-24 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xidmetler_app', '0002_delete_xidmətlərimiz_haqqında'),
    ]

    operations = [
        migrations.CreateModel(
            name='Xidmətlərimiz_Haqqında',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('esas_foto', models.ImageField(upload_to='media/')),
                ('haqqimizda_ust_yazi_1', models.TextField(help_text='Maksimum 500 hərif', max_length=500)),
                ('haqqimizda_ust_yazi_2', models.TextField(help_text='Maksimum 500 hərif', max_length=500)),
                ('xett_foto', models.ImageField(upload_to='media/')),
                ('metn', models.TextField(help_text='Maksimum 10000 hərif', max_length=10000)),
            ],
        ),
    ]
