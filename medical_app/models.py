from django.db import models
from django.db.models.base import Model
from django.db.models.fields.files import ImageField
from django.utils.translation import gettext_lazy as _
from django.utils.html import mark_safe
from django.utils import timezone

#Ana sehfe basgligi

class SaytınBaşlığı(models.Model):
    bashlig = models.CharField(max_length=20, help_text="Maksimum 20 hərif")

    def __str__(self):
        return self.bashlig

class SaytınBaşlığıFoto(models.Model):
    bashligsekil = models.ImageField(upload_to='media/', blank=True)

class LogoŞəkilAnaSəhifə(models.Model):
    logosekilana = models.ImageField(upload_to='media/')

class BaşlıqNömrəEpoct(models.Model):
    number = models.CharField(max_length=20, help_text="Maksimum 20 hərif")
    email = models.CharField(max_length=30, help_text="Maksimum 30 hərif")
    clock = models.CharField(max_length=200,help_text="Maksimum 200 hərif")

    def __str__(self):
        return self.email

class GirişŞəkilYazılar(models.Model):
    yazi_1 = models.CharField(max_length=50, help_text="Maksimum 50 hərif") 
    yazi_2 = models.CharField(max_length=30, help_text="Maksimum 30 hərif")

    def __str__(self):
        return self.yazi_1

class GirişŞəkil(models.Model):
    image = models.ImageField(upload_to='images', help_text="Tam keyfiyyətti 1282x700 ölçüsündə foto yükləməyinizin məsləhət görünür...")


class HaqqımızdaŞəkillər(models.Model):
    esas_sekil = models.ImageField(upload_to='media/', help_text="Fotonu olcuye uygun yukleyin...")
    orta_sekil = models.ImageField(upload_to='media/', help_text="Kicik foto yukluyun...")


class HaqqımızdaYazılar(models.Model):
    yazi_2 = models.CharField(max_length=35, help_text="Maksimum 35 hərif")
    yazi_3 = models.TextField(max_length=200, help_text="Maksimum 200 hərif")
    yazi_4 = models.TextField(max_length=5000, help_text="Maksimum 5000 hərif")

    def __str__(self):
        return self.yazi_2

class Haqqımızdamüəllif(models.Model):
    adsoyad = models.CharField(max_length=50, help_text="Maksimum 50 hərif")
    vezife = models.CharField(max_length=30, help_text="Maksimum 30 hərif")


class Servis_Üst_Yazılar(models.Model):
    yazi_1 = models.CharField(max_length=15, help_text="Maksimum 15 hərif")
    yazi_2 = models.CharField(max_length=30, help_text="Maksimum 30 hərif")

    def __str__(self):
        return self.yazi_1

class Servis_Məlümat_AnaSəhifə(models.Model):
    balaca_sekil_hecmi_244_x_80 = models.ImageField(upload_to = 'media/', help_text="Fotonun həcmi 244 uzunluğu 80 enni olmalıdır (244x80)")
    servis_ust_yazi = models.CharField(max_length=30, help_text="Maksimum 30 hərif")
    servis_kicik_melumat = models.TextField(max_length=250, help_text="Maksimum 250 hərif")


    def __str__(self):
        return self.servis_ust_yazi       

class MəlumatSektoru(models.Model):
    kicik_yazi = models.TextField(max_length=200, help_text="Maksimum 200 hərif")
    boyuk_yazi = models.TextField(max_length=150, help_text="Maksimum 150 hərif")

    def __str__(self):
        return self.kicik_yazi

class MükafatSektoru(models.Model):
    baslig_1 = models.CharField(max_length=20, help_text="Maksimum 20 hərif")
    sagalmis_xestelerin_sayi = models.CharField(max_length=15, help_text="Maksimum 15 hərif")
    kicik_metn_1 = models.TextField(max_length=250, help_text="Maksimum 250 hərif")
    baslig_2 = models.CharField(max_length=20, help_text="Maksimum 20 hərif")
    mukafatlarin_sayi = models.CharField(max_length=15, help_text="Maksimum 15 hərif")
    kicik_metn_2 = models.TextField(max_length=250, help_text="Maksimum 250 hərif")

    def __str__ (self):
        return self.baslig_1




# class TəciliInfo(models.Model):
#     basliq = models.CharField(max_length=60,help_text="Maksimum 60 hərif")
#     elaqenomresi = models.CharField(max_length=50, help_text="Maksimum 50 hərif")

#     def __str__(self):
#         return self.basliq

# class TəciliElektron_Əlaqe(models.Model):
#     metn = models.TextField(max_length=250, help_text="Maksimum 250 hərif")
#     elaqepoct = models.EmailField(max_length=80, help_text="Maksimum 80 hərif")
#     mekan = models.CharField(max_length=100, help_text="Maksimum 100 hərif")

#     def __str__(self):
#         return self.metn

class PasiyentlərinRəyi_Slayder(models.Model):
    foto = models.ImageField(upload_to="media/", help_text="1080x1323 həcmində foto yükləməyinizi Məsləhət görünür")
    vaxt = models.DateField(default=timezone.now,help_text="Avtomatik ozü vaxtı təyin edir")
    metn = models.TextField(max_length=300, help_text="Maksimum 300 hərif")
    instagram = models.CharField(max_length=40, help_text="Maksimum 40 hərif")

    def __str__(self):
        return self.metn


class Tez_Tez_VerilənSualların_Foto(models.Model):
    ust_foto = models.ImageField(upload_to='media/', help_text="462x480 həcmində foto yükləməyinizi Məsləhət görünür")
    alt_foto = models.ImageField(upload_to='media/', help_text="480x350 həcmində foto yükləməyinizi Məsləhət görünür")
    yan_foto = models.ImageField(upload_to='media/', help_text="276x314 həcmində foto yükləməyinizi Məsləhət görünür")


class Tez_Tez_VerilənSuallar(models.Model):
    sual = models.TextField(max_length=200, help_text="Maksimum 200 hərif")
    cavab = models.TextField(max_length=1000, help_text="Maksimum 1000 hərif")

    def __str__(self):
        return self.sual


class Footer_Bloq(models.Model):
    foto_1 = models.ImageField(upload_to='media/')
    bloq_1_seyfenin_bashliq_postu = models.TextField(max_length=300, help_text="Maksimum 300 hərif")
    vaxt_1 = models.DateField()

    foto_2 = models.ImageField(upload_to='media/')
    bloq_2_seyfenin_bashliq_postu = models.TextField(max_length=300, help_text="Maksimum 300 hərif")
    vaxt_2 = models.DateField()

    foto_3 = models.ImageField(upload_to='media/')
    bloq_3_seyfenin_bashliq_postu = models.TextField(max_length=300, help_text="Maksimum 300 hərif")
    vaxt_3 = models.DateField()

class Youtube_Link_Əsas(models.Model):
    youtube_link = models.TextField(max_length=5000, help_text="Youtube Video Linki")

class MobileFoto(models.Model):
    foto_res = models.ImageField(upload_to='media/')

class SEO_AnaSəhifə(models.Model):
    metatag = models.TextField()