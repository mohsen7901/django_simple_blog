from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['website:index', 'website:about', 'website:contact', 'website:services', 'website:portfolio', 'website:portfolio_details']

    def location(self, item):
        return reverse(item)