from django.db import models


class ƏsasFoto(models.Model):
    esas_foto = models.ImageField(upload_to="media/")

class ƏsasFoto_ÜstYazılar(models.Model):
    metn_1 = models.TextField(max_length=100, help_text="Maksimum 100 hərif")
    metn_2 = models.TextField(max_length=80, help_text="Maksimum 100 hərif")

    def __str__(self):
        return self.metn_1


class Xidmətlərimiz_Haqqında(models.Model):
    esas_foto = models.ImageField(upload_to='media/')
    haqqimizda_ust_yazi_1 = models.TextField(max_length=500, help_text="Maksimum 500 hərif")
    haqqimizda_ust_yazi_2 = models.TextField(max_length=500, help_text="Maksimum 500 hərif")
    xett_foto = models.ImageField(upload_to='media/')
    metn = models.TextField(max_length=10000,help_text="Maksimum 10000 hərif")

    def __str__(self):
        return self.metn


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


