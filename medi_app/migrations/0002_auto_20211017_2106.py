# Generated by Django 3.2.7 on 2021-10-17 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medi_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Müsahibə',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(help_text='Fotonun həcmi 570 uzunluğu 700 enni olmalıdır (570x700)', upload_to='media/')),
                ('link_musahibe', models.CharField(help_text='Maksimum 40 simvol', max_length=40)),
            ],
        ),
        migrations.DeleteModel(
            name='MediaŞəkil',
        ),
        migrations.RenameField(
            model_name='mediatvproqramları',
            old_name='yazı_1',
            new_name='link_tv',
        ),
        migrations.RenameField(
            model_name='mediayoutube',
            old_name='link',
            new_name='link_youtube',
        ),
        migrations.RemoveField(
            model_name='mediatvproqramları',
            name='yazı_2',
        ),
    ]
