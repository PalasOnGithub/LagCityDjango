from django.contrib import sitemaps
from django.urls import reverse
from .models import*


class StaticViewSitemapGame(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['home_game', 'games', 'blog', 'faq_page', 'contact_page']

    def location(self, item):
        return reverse(item)


class Game_Sitemap(sitemaps.Sitemap):
    changefreq = "hourly"
    priority = 0.7

    def items(self):
        return Game.objects.all()

    def lastmod(self, obj): 
        return obj.create_on

class News_Sitemap(sitemaps.Sitemap):
    changefreq = "hourly"
    priority = 0.7

    def items(self):
        return News.objects.all()


    def lastmod(self, obj): 
        return obj.create_on


