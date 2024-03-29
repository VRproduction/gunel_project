# Generated by Django 3.2.7 on 2021-10-29 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medical_app', '0087_auto_20211018_2121'),
    ]

    operations = [
        migrations.CreateModel(
            name='Footer_Bloq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(upload_to='media/')),
                ('bloq_seyfenin_bashliq_postu', models.TextField(help_text='Maksimum 300 hərif', max_length=300)),
                ('vaxt', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='Bloq_YeniXəbərlər_AnaSehifə',
        ),
        migrations.DeleteModel(
            name='BloqSolMətn',
        ),
    ]
