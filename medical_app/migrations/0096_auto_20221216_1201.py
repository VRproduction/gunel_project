# Generated by Django 3.2.15 on 2022-12-16 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medical_app', '0095_seo_anasəhifə'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SEO_AnaSəhifə',
        ),
        migrations.AlterField(
            model_name='saytınbaşlığı',
            name='bashlig',
            field=models.CharField(help_text='Maksimum 1000 hərif', max_length=1000),
        ),
    ]
