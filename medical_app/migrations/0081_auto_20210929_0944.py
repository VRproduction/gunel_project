# Generated by Django 3.2.7 on 2021-09-29 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medical_app', '0080_alter_pasiyentlərinrəyi_slayder_foto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tez_Tez_VerilənSuallar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sual', models.TextField(help_text='Maksimum 150 hərif', max_length=150)),
                ('cavab', models.TextField(help_text='Maksimum 250 hərif', max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Tez_Tez_VerilənSualların_Foto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ust_foto', models.ImageField(help_text='462x480 həcmində foto yükləməyinizi Məsləhət görünür', upload_to='media/')),
                ('alt_foto', models.ImageField(help_text='480x350 həcmində foto yükləməyinizi Məsləhət görünür', upload_to='media/')),
                ('yan_foto', models.ImageField(help_text='276x314 həcmində foto yükləməyinizi Məsləhət görünür', upload_to='media/')),
            ],
        ),
        migrations.AlterField(
            model_name='pasiyentlərinrəyi_slayder',
            name='foto',
            field=models.ImageField(help_text='1080x1323 həcmində foto yükləməyinizi Məsləhət görünür', upload_to='media/'),
        ),
    ]
