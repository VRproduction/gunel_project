# Generated by Django 3.2.7 on 2021-09-28 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medical_app', '0079_auto_20210928_1226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pasiyentlərinrəyi_slayder',
            name='foto',
            field=models.ImageField(help_text='Məsləhət görünür 1080x1323 foto yükləməyinizi.', upload_to='media/'),
        ),
    ]
