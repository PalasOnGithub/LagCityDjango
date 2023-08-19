from django.contrib import sitemaps
from django.urls import reverse
from .models import*


class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['home_music', 'about', 'artict' , 'contacts' , 'thanks_feedback', 'News', 'privacy_page', 'releases_song']

    def location(self, item):
        return reverse(item)

class Singer_Sitemap(sitemaps.Sitemap):
    changefreq = "hourly"
    priority = 0.7

    def items(self):
        return Singer.objects.all()

    def lastmod(self, obj): 
        return obj.create_on



class Album_Sitemap(sitemaps.Sitemap):
    changefreq = "hourly"
    priority = 0.7

    def items(self):
        return Album.objects.all()

    def lastmod(self, obj): 
        return obj.create_on


class Track_Sitemap(sitemaps.Sitemap):
    changefreq = "hourly"
    priority = 0.7

    def items(self):
        return Track.objects.all()

    def lastmod(self, obj): 
        return obj.create_on

class Event_Sitemap(sitemaps.Sitemap):
    changefreq = "hourly"
    priority = 0.7

    def items(self):
        return Event.objects.all()

    def lastmod(self, obj): 
        return obj.create_on



