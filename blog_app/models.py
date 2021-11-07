from django.db import models
from django.utils import timezone

# Create your models here.
class ƏsasFoto(models.Model):
    esas_foto = models.ImageField(upload_to='media/')

class ƏsasFoto_ÜstMətn(models.Model):
    metn_1 = models.TextField(max_length=100, help_text="Maksimum 100 hərif")
    metn_2 = models.TextField(max_length=150, help_text="Maksimum 150 hərif")

    def __str__(self):
        return self.metn_1

class PostPaylaşılma(models.Model):
    foto_post = models.ImageField(upload_to='media/', help_text="770x561 Həcmində foto yükləməyinizi məsləhət görünür")
    vaxt = models.DateTimeField(default=timezone.now, help_text="Vaxtı avtomatik olaraq ozü təyin edəcək")
    ad_soyad = models.CharField(max_length=80, help_text="Maksimum 80 hərif")
    metinin_bashligi = models.TextField(max_length=150, help_text="Maksimum 150 hərif")
    metn = models.TextField(max_length=800, help_text="Maksimum 800 hərif")

    def __str__(self):
        return self.metinin_bashligi

class SosialŞəbəkəLinkləri(models.Model):
    facebook_url = models.TextField(max_length=500, help_text="FaceBook profilinizin Linki")
    youtube_url = models.TextField(max_length=500, help_text="YouTube kanalinizin Linki")
    instagram_url = models.TextField(max_length=500, help_text="Instagram profilinizin Linki")

    def __str__(self):
        return self.facebook_url


class Hekayə(models.Model):
    hekaye = models.TextField(max_length=500, help_text="Maksimum 500 hərif")
    muellif = models.CharField(max_length=80, help_text="Maksimum 80 hərif")

    def __str__(self):
        return self.hekaye