# Generated by Django 3.2.7 on 2021-09-22 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qebul_app', '0004_auto_20210922_0927'),
    ]

    operations = [
        migrations.CreateModel(
            name='Qəbul_Haqqımızda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ust_metn', models.CharField(help_text='Maksimum 30 simvol', max_length=30)),
                ('kicik_metn', models.CharField(help_text='Maksimum 35 simvol', max_length=35)),
                ('etrafli_melumat', models.TextField(help_text='Maksimum 200 simvol', max_length=200)),
                ('ust_metn_1', models.CharField(help_text='Maksimum 30 simvol', max_length=30)),
                ('kicik_metn_1', models.TextField(help_text='Maksimum 150 simvol', max_length=150)),
                ('ust_metn_2', models.CharField(help_text='Maksimum 30 simvol', max_length=30)),
                ('kicik_metn_2', models.TextField(help_text='Maksimum 150 simvol', max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Qəbul_Haqqımızda_foto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('esasfoto', models.ImageField(upload_to='media/')),
                ('ortafoto', models.ImageField(upload_to='media/')),
            ],
        ),
        migrations.AlterField(
            model_name='əsas_şəkilin_yazıları',
            name='yazı_1',
            field=models.CharField(help_text='Maksimum 80 simvol', max_length=80),
        ),
        migrations.AlterField(
            model_name='əsas_şəkilin_yazıları',
            name='yazı_2',
            field=models.CharField(help_text='Maksimum 35 simvol', max_length=35),
        ),
    ]
