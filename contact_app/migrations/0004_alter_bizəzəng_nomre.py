# Generated by Django 3.2.7 on 2021-09-28 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_app', '0003_alter_bizəzəng_nomre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bizəzəng',
            name='nomre',
            field=models.CharField(help_text='Maksimum 50 simvol', max_length=50),
        ),
    ]
