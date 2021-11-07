# Generated by Django 3.2.7 on 2021-09-19 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medical_app', '0040_haqimizdasekiller'),
    ]

    operations = [
        migrations.CreateModel(
            name='MelumatSektoru',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kicik_yazi', models.CharField(help_text='Maksimum 35 simvol', max_length=35)),
                ('boyuk_yazi', models.CharField(help_text='Maksimum 60 simvol', max_length=60)),
            ],
        ),
        migrations.AlterField(
            model_name='bashlignomreepoct',
            name='email',
            field=models.CharField(help_text='Maksimum 30 simvol', max_length=30),
        ),
        migrations.AlterField(
            model_name='bashlignomreepoct',
            name='number',
            field=models.CharField(help_text='Maksimum 20 simvol', max_length=20),
        ),
        migrations.AlterField(
            model_name='haqqimizdamuellif',
            name='adsoyad',
            field=models.CharField(help_text='Maksimum 30 simvol', max_length=30),
        ),
        migrations.AlterField(
            model_name='haqqimizdamuellif',
            name='vezife',
            field=models.CharField(help_text='Maksimum 15 simvol', max_length=15),
        ),
        migrations.AlterField(
            model_name='haqqimizdayazilar',
            name='yazi_1',
            field=models.CharField(help_text='Maksimum 30 simvol', max_length=30),
        ),
        migrations.AlterField(
            model_name='haqqimizdayazilar',
            name='yazi_2',
            field=models.CharField(help_text='Maksimum 35 simvol', max_length=35),
        ),
        migrations.AlterField(
            model_name='haqqimizdayazilar',
            name='yazi_3',
            field=models.TextField(help_text='Maksimum 200 simvol', max_length=200),
        ),
        migrations.AlterField(
            model_name='haqqimizdayazilar',
            name='yazi_4',
            field=models.TextField(help_text='Maksimum 300 simvol', max_length=300),
        ),
        migrations.AlterField(
            model_name='komandayazi',
            name='komanda',
            field=models.CharField(help_text='Maksimum 20 simvol', max_length=20),
        ),
        migrations.AlterField(
            model_name='komandayazi',
            name='komandayazi',
            field=models.CharField(help_text='Maksimum 30 simvol', max_length=30),
        ),
        migrations.AlterField(
            model_name='saytbashlig',
            name='bashlig',
            field=models.CharField(help_text='Maksimum 20 simvol', max_length=20),
        ),
        migrations.AlterField(
            model_name='servismelumatanaseyfe',
            name='servis_kicik_melumat',
            field=models.TextField(help_text='Maksimum 250 simvol', max_length=250),
        ),
        migrations.AlterField(
            model_name='servismelumatanaseyfe',
            name='servis_ust_yazi',
            field=models.CharField(help_text='Maksimum 30 simvol', max_length=30),
        ),
        migrations.AlterField(
            model_name='servisustyazilar',
            name='yazi_1',
            field=models.CharField(help_text='Maksimum 15 simvol', max_length=15),
        ),
        migrations.AlterField(
            model_name='servisustyazilar',
            name='yazi_2',
            field=models.CharField(help_text='Maksimum 30 simvol', max_length=30),
        ),
        migrations.AlterField(
            model_name='slayderyazilar',
            name='yazi_1',
            field=models.CharField(help_text='Maksimum 50 simvol', max_length=50),
        ),
        migrations.AlterField(
            model_name='slayderyazilar',
            name='yazi_2',
            field=models.CharField(help_text='Maksimum 30 simvol', max_length=30),
        ),
    ]
