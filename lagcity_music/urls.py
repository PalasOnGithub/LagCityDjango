from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.sitemaps.views import sitemap
from azbankgateways.urls import az_bank_gateways_urls
from part1.sitemaps import*
from part2.sitemaps import*

sitemaps = {
    'static': StaticViewSitemap,
    'singer':Singer_Sitemap,
    'album':Album_Sitemap,
    'track':Track_Sitemap,
    'event':Event_Sitemap,
    'game': Game_Sitemap,
    'news': News_Sitemap,
    'yt':StaticViewSitemapGame,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('music/',include('part1.urls')),
    path('game/',include('part2.urls')),
    path('accounts/',include('allauth.urls')),
    path('takepic/', include('part4.urls')),
    path('bankgateways/', az_bank_gateways_urls()),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
    name='django.contrib.sitemaps.views.sitemap')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
handler404 = 'part1.views.error_404'

