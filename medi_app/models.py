from django.db import models
from django.db.models.fields.files import ImageField

# Create your models here.

class MediaƏsasŞəkil(models.Model):
    foto = models.ImageField(upload_to='media/')

class ƏsasŞəkilin_ÜstMətini(models.Model):
    yazı_1 = models.TextField(max_length=80, help_text="Maksimum 80 simvol")
    yazı_2 = models.TextField(max_length=70, help_text="Maksimum 70 simvol")

    def __str__(self):
        return self.yazı_1

class Müsahibe(models.Model):
    foto = models.ImageField(upload_to='media/', help_text="Fotonun həcmi 570 uzunluğu 700 enni olmalıdır (570x700)")
    link_musahibe = models.CharField(max_length=40, help_text="Maksimum 40 simvol")
    metn = models.TextField(max_length=1000, help_text="Kicik metn")

    def __str__(self):
        return self.link_musahibe

class MediaTvProqramları(models.Model):
    foto = models.ImageField(upload_to='media/', help_text="Fotonun həcmi 570 uzunluğu 700 enni olmalıdır (570x700)")
    link_tv = models.CharField(max_length=40, help_text="Maksimum 40 simvol")
    metn = models.TextField(max_length=1000, help_text="Kicik metn")

    def __str__(self):
        return self.link_tv

class MediaYouTube(models.Model):
    foto = models.ImageField(upload_to='media/', help_text="Fotonun həcmi 570 uzunluğu 700 enni olmalıdır (570x700)")
    link_youtube = models.TextField(max_length=200, help_text="Videonuzun Linkini Yükləyin")
    metn = models.TextField(max_length=1000, help_text="Kicik metn")

    def __str__(self):
        return self.link_youtube

