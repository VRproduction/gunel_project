from django.db import models


class ConferenceSeo(models.Model):
    title = models.CharField(null=True, blank=True, max_length=255)
    description = models.TextField(null=True, blank=True)
    keyword = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Konfrans SEO'
        verbose_name_plural = 'Konfrans SEO'


class BlogSeo(models.Model):
    title = models.CharField(null=True, blank=True, max_length=255)
    description = models.TextField(null=True, blank=True)
    keyword = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Bloq SEO'
        verbose_name_plural = 'Bloq SEO'


class AppointmentSeo(models.Model):
    title = models.CharField(null=True, blank=True, max_length=255)
    description = models.TextField(null=True, blank=True)
    keyword = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Qəbula yazıl SEO'
        verbose_name_plural = 'Qəbula yazıl SEO'


class ContactSeo(models.Model):
    title = models.CharField(null=True, blank=True, max_length=255)
    description = models.TextField(null=True, blank=True)
    keyword = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Əlaqə SEO'
        verbose_name_plural = 'Əlaqə SEO'


class HomeSeo(models.Model):
    title = models.CharField(null=True, blank=True, max_length=255)
    description = models.TextField(null=True, blank=True)
    keyword = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Ana səhifə SEO'
        verbose_name_plural = 'Ana səhifə SEO'


class ServiceSeo(models.Model):
    title = models.CharField(null=True, blank=True, max_length=255)
    description = models.TextField(null=True, blank=True)
    keyword = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Xidmətlər SEO'
        verbose_name_plural = 'Xidmətlər SEO'


class MediaSeo(models.Model):
    title = models.CharField(null=True, blank=True, max_length=255)
    description = models.TextField(null=True, blank=True)
    keyword = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Media SEO'
        verbose_name_plural = 'Media SEO'
