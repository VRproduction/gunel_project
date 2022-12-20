from django.contrib.sitemaps import Sitemap
from blog_app.models import PostPaylaşılma
from xidmetler_app.models import Xidmətlərimiz_Haqqında
from django.urls import reverse


class BlogSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.8
    protocol = 'https'

    def items(self):
        return PostPaylaşılma.objects.all()

    def lastmod(self, obj):
        return obj.vaxt

    def location(self, obj):
        return '/blog/%s' % (obj.slug)


class ServiceSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.8
    protocol = 'https'

    def items(self):
        return Xidmətlərimiz_Haqqında.objects.all()

    def lastmod(self, obj):
        return obj.created_at

    def location(self, obj):
        return '/xidmetlerimiz/%s' % (obj.slug)


class StaticSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = 'https'

    def items(self):
        return [
            'homepage', 'konfrans', 'media',
            'blog', 'xidmetler', 'contact', 'appoinment'
        ]

    def location(self, item):
        return reverse(item)
