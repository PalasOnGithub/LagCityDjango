# BAROON BY 2 DIG, OOMRAN ;)

from django.urls import path, include
from .views import*

urlpatterns = [
    path('', HomePage, name = 'home_music'), #ᑕᕼEᑕK
    path('about_us', AboutUsPage, name = 'about'), #ᑕᕼEᑕK
    path('news/<int:nuk>', Detail_newPage, name = 'detail_new'), #ᑕᕼEᑕK
    path('artist/<int:num>', Detail_artistPage, name = 'detail_artist'), #ᑕᕼEᑕK
    path('artists', ListArtistPage , name = 'artict'), #ᑕᕼEᑕK
    path('contact_us', ContactPage , name = 'contacts'), #ᑕᕼEᑕK
    path('Thanks', Thankpage, name = 'thanks_feedback'), #ᑕᕼEᑕK
    path('news', NewsPage, name = 'News'), #ᑕᕼEᑕK
    path('privacy', PrivacyPage, name = 'privacy_page'), #ᑕᕼEᑕK
    path('release/<int:nus>', Detail_SongPage, name = 'detail_song'), #ᑕᕼEᑕK
    path('release/album/<int:nuc>', Detail_AlbumPage, name = 'detail_album'), #ᑕᕼEᑕK
    path('releases', ReleasesSongPage, name = 'releases_song'), #ᑕᕼEᑕK
    path('releases/album', ReleasesAlbumPage, name = 'releases_album'), #ᑕᕼEᑕK
    path('resault', ResaultPage, name="search"),
    path('playlists', PlayListPage, name='main_playlist'),
    path('playlist/<int:num>', PlayListDetailPage, name='detail_playlist'),
    path('buy_sub', price_lag, name='buy_sub_page'),
    path('go-to-bank', go_to_gateway_view),
    path('callback-gateway', callback_gateway_view),
    path('sub_fail', sub_fail_view)
]
 