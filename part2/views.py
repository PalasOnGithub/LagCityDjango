from multiprocessing import context
from django.shortcuts import render, redirect
from .models import*
import random
# Create your views here.

items = list(Game.objects.all())

def HomePage(request):
    last_game = Game.objects.all().order_by('-id')[:6]
    random_items = random.sample(items, 2)
    last_news = News.objects.all().order_by('-id')[:4]

    context= {
        'new_g' : last_game,
        'random_game' : random_items,
        'last_news' : last_news,
    }
    return render(request, 'game/index.html', context)


def DetailPageGame(request, num):
    game = Game.objects.get(pk=num)

    context = {
        'game':game,
    }
    return render(request , 'game/single-game.html', context)

def PageGame(request):
    all_games = Game.objects.all()

    context = {
        'all_game': all_games
    }
    return render(request , 'game/games.html', context)

def BlogPage(request):
    akhbar = News.objects.all()

    context = {
        'news':akhbar,
    }
    return render(request, 'game/blog.html', context)

def DetailBlogPage(request, num):
    game = News.objects.get(pk=num)
    last_game = Game.objects.all().order_by('-id')[:6]
    last_news = News.objects.all().order_by('-id')[:4]
    comment_hash = Comment.objects.filter(for_Track__id=num)

    context = {
        'game':game,
        "last_game":last_game,
        "news":last_news,
        'comment':comment_hash,
    }
    return render(request , 'game/blog-details.html', context)

def Thankcomment(request):
    if request.method == 'POST':
        form_name = request.POST['username']
        form_email = request.POST['email']
        form_text = request.POST['body']
        fromf = request.POST['ggs']
        g = Comment(for_Track = News.objects.get(id = fromf) , name=form_name , email=form_email , body=form_text)
        g.save()
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect('/game')

def FaqPage(request):
    return render(request, 'game/faq.html')

def ContactPage(request):
    return render(request, 'game/contact.html')

def GotContact(request):
    if request.method == "POST":
        form_name = request.POST['username']
        form_email = request.POST['email']
        form_text = request.POST['subject']
        fromf = request.POST['text']
        con = Contact_to_us(name=form_name,email= form_email,subject= form_text,Message= fromf)
        con.save()
        return redirect(request.META.get('HTTP_REFERER'))



