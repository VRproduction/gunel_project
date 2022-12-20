from django.db import models
from django.utils import timezone


class ƏsasFoto(models.Model):
    esas_foto = models.ImageField(upload_to="media/")

class ƏsasFoto_ÜstYazılar(models.Model):
    metn_2 = models.TextField(max_length=80, help_text="Maksimum 100 hərif")

    def __str__(self):
        return self.metn_2


class Xidmətlərimiz_Haqqında(models.Model):
    esas_foto = models.ImageField(upload_to='media/')
    logo = models.ImageField(upload_to = 'media/services/',
                             help_text="Fotonun həcmi 244 uzunluğu 80 enni olmalıdır (244x80)",
                             null=True, blank=True)
    haqqimizda_ust_yazi_1 = models.TextField(max_length=500, help_text="Maksimum 500 hərif")
    haqqimizda_ust_yazi_2 = models.TextField(max_length=500, help_text="Maksimum 500 hərif")
    xett_foto = models.ImageField(upload_to='media/')
    metn = models.TextField(max_length=10000,help_text="Maksimum 10000 hərif")
    created_at = models.DateTimeField(default=timezone.now, help_text="Vaxtı avtomatik olaraq özü təyin edəcək")
    description = models.TextField(max_length=50000, null=True, blank=True)
    title = models.TextField(max_length=50000, null=True, blank=True)
    keyword = models.TextField(max_length=50000, null=True, blank=True)
    slug = models.SlugField(db_index=True, max_length=500, null=True, blank=True)

    @property
    def sitemap_image(self):
        return self.esas_foto.url if self.esas_foto else None

    def __str__(self):
        return self.metn

    class Meta:
        verbose_name = 'Xidmətlər'
        verbose_name_plural = 'Xidmətlər'


# class ServisMəlumat(models.Model):
#     sag_melumat = models.CharField(max_length=50, help_text="Maksimum 50 hərif")

#     def __str__(self):
#         return self.sag_melumat

# class DigərServislər(models.Model):
#     servisin_adi = models.CharField(max_length=50, help_text="Maksimum 50 hərif")
    
#     def __str__(self):
#         return self.servisin_adi

# class Sagbaner(models.Model):
#     sag_baner = models.ImageField("media/", help_text="Fotonun həcmi 470 uzunluğu 600 enni olmalıdır (470x600)")


class Məlumat_Sektoru(models.Model):
    kicik_metn = models.TextField(max_length=500, help_text="Maksimum 500 hərif")
    bashliq = models.TextField(max_length=1500, help_text="Maksimum 1500 hərif")

    def __str__(self):
        return self.bashliq

class Xidmətlər_Postları(models.Model):
    foto = models.ImageField(upload_to='media/')
    bashliq = models.TextField(max_length=1000)
    vaxt = models.DateTimeField()

    def __str__(self):
        return self.bashliq