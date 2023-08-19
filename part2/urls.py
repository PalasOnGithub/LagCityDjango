# BAROON BY 2 DIG, OOMRAN ;)
from django.urls import path, include
from .views import*

urlpatterns = [
    path('', HomePage, name = 'home_game'), #ᑕᕼEᑕK
    path('detail/<int:num>/', DetailPageGame, name= 'detail_game'),
    path('games', PageGame , name = 'games'),
    path('blog', BlogPage , name = 'blog'),
    path('detail/blog/<int:num>/', DetailBlogPage, name= 'detail_blog'),
    path('thanks_for_comment', Thankcomment , name = "got_comment"),
    path('faq', FaqPage , name = 'faq_page'),
    path('contact_us', ContactPage, name = 'contact_page'),
    path('thanks_forit', GotContact, name = 'give_me_money')
]
 