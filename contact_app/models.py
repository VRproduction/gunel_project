from django.db import models

# Create your models here.

class ƏsasFotoMətnlər(models.Model):
    metn_1 = models.TextField(max_length=80, help_text='Maksimum 80 hərif')
    metn_2 = models.TextField(max_length=200, help_text='Maksimum 200 hərif')

    def __str__(self):
        return self.metn_1

class Gmail(models.Model):
    gmail = models.EmailField(max_length=50, help_text='Maksimum 50 hərif')

    def __str__(self):
        return self.gmail

class Məkan(models.Model):
    mekan = models.TextField(max_length=100, help_text='Maksimum 100 həif')

    def __str__(self):
        return self.mekan

class BizəZəng(models.Model):
    nomre = models.CharField(max_length=50,help_text='Maksimum 50 simvol')

    def __str__(self):
        return self.nomre


class Üst_Şəkil(models.Model):
    img = models.ImageField('media/')

class MobileƏsasFoto(models.Model):
    img = models.ImageField('media/')