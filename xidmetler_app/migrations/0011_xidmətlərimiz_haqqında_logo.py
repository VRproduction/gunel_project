# Generated by Django 3.2.15 on 2022-12-20 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xidmetler_app', '0010_xidmətlərimiz_haqqında_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='xidmətlərimiz_haqqında',
            name='logo',
            field=models.ImageField(blank=True, help_text='Fotonun həcmi 244 uzunluğu 80 enni olmalıdır (244x80)', null=True, upload_to='media/services/'),
        ),
    ]
