# Generated by Django 3.2.7 on 2021-09-20 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medical_app', '0056_auto_20210920_0933'),
    ]

    operations = [
        migrations.CreateModel(
            name='BloqXeberlerAnaSeyfe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(upload_to='media/')),
                ('kicikmetn', models.CharField(help_text='Maksimum 200 simvol', max_length=200)),
                ('ustmetn', models.TextField(help_text='Maksimum 80 simvol', max_length=80)),
                ('etraflimelumat', models.TextField(help_text='Maksimum 250 simvol', max_length=250)),
            ],
        ),
        migrations.AlterField(
            model_name='bloqsolmetn',
            name='boyukyazi',
            field=models.TextField(help_text='Maksimum 45 simvol', max_length=45),
        ),
    ]
