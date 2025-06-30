from django.contrib.sitemaps import Sitemap

from .models import Engine, Logistic, Handyman

class EngineSitemap(Sitemap):
    changefreq = 'yearly'
    priority = 0.9

    def items(self):
        return Engine.objects.all()

    def lastmod(self, obj):
        return obj.updated

class LogisticSitemap(Sitemap):
    changefreq = 'yearly'
    priority = 0.9

    def items(self):
        return Logistic.objects.all()

    def lastmod(self, obj):
        return obj.updated

class HandymanSitemap(Sitemap):
    changefreq = 'yearly'
    priority = 0.9

    def items(self):
        return Handyman.objects.all()

    def lastmod(self, obj):
        return obj.updated