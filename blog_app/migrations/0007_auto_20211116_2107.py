# Generated by Django 3.2.7 on 2021-11-16 21:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0006_digər_bloqlar_footer_açılış_vaxtları_footer_yazısı_haqqımda_məlumat_i̇nstagram_postları'),
    ]

    operations = [
        migrations.RenameField(
            model_name='footer_açılış_vaxtları',
            old_name='vaxt_1',
            new_name='acilis_vaxti',
        ),
        migrations.RenameField(
            model_name='footer_açılış_vaxtları',
            old_name='vaxt_2',
            new_name='baglanan_vaxt',
        ),
    ]