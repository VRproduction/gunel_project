from django.db import models
from django.db.models.fields.files import ImageField

# Create your models here.

class Əsas_Şəkil(models.Model):
    esassekil = models.ImageField(upload_to='media/')

class Əsas_Şəkilin_Yazıları(models.Model):
    yazı_1 = models.CharField(max_length=80, help_text="Maksimum 80 simvol")
    yazı_2 = models.CharField(max_length=35, help_text="Maksimum 35 simvol")

    def __str__(self):
        return self.yazı_1

class Qəbul_Haqqımızda_foto(models.Model):
    esasfoto = models.ImageField(upload_to='media/')
    ortafoto = models.ImageField(upload_to='media/')
    youtube_url = models.TextField(max_length=500, help_text="Youtube kanalınızın linki")

class Qəbul_Haqqımızda(models.Model):
    ust_metn = models.CharField(max_length=30, help_text="Maksimum 30 simvol")
    kicik_metn = models.CharField(max_length=35, help_text="Maksimum 35 simvol")
    etrafli_melumat = models.TextField(max_length=200, help_text="Maksimum 200 simvol")
    ust_metn_1 = models.CharField(max_length=30, help_text="Maksimum 30 simvol")
    kicik_metn_1 = models.TextField(max_length=150, help_text="Maksimum 150 simvol")
    ust_metn_2 = models.CharField(max_length=30, help_text="Maksimum 30 simvol")
    kicik_metn_2 = models.TextField(max_length=150, help_text="Maksimum 150 simvol")

    def __str__(self):
        return self.ust_metn

class Qəbul_Form_Arxa_Foto(models.Model):
    foto = models.ImageField(upload_to='media/')

class QəbulXəritə(models.Model):
    xerite_url = models.TextField(max_length=500, help_text='Google Xəritənin Linki')

    def __str__(self):
        return self.xerite_url

class Qəbula_Yazıl_Forma_Arxa_Foto(models.Model):
    foto = models.ImageField(upload_to='media/')

