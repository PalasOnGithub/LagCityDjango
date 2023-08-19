from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import*
import random
import datetime
from django.db.models import Q
from django.contrib.auth.models import Permission
import logging
from django.urls import reverse
from azbankgateways import bankfactories, models as bank_models, default_settings as settings
from azbankgateways.exceptions import AZBankGatewaysException
from .custom_dec import require_common_user
from django.contrib.auth.decorators import login_required
from datetime import datetime



# Create your views here.


def HomePage(request):
	home_pic = HomeBack.objects.get(id=1)
	print(request)
	items = list(Track.objects.all())
	user_com = request.user
	try:
		find_user = Plant.objects.get(from_user=user_com)
	except:
		find_user = None
		pass
	Random_ahang = random.choice(items)
	new_ahang = Track.objects.all()[:5]
	new_artists = Singer.objects.all()[:5]
	old_ahang = Track.objects.all()[:5]
	new_album = Album.objects.all()[:5]
	new_News = Event.objects.all()[:5]

	context = {
		'random_ahang':Random_ahang,
		'new_ahang':new_ahang,
		'new_artist':new_artists,
		'old_ahang':old_ahang,
		"new_album" : new_album,
		"new_News": new_News,
		"sub":find_user,
		"home_pic": home_pic,
		"know":find_user,
	}
	
	return render(request, 'music/index.html', context)

def AboutUsPage(request):
	return render(request, 'music/about.html')

def Detail_newPage(request, nuk):
	etc = Event.objects.get(pk=nuk)
	context = {
		'etc': etc,
	}
	return render(request, 'music/article.html', context)

def Detail_artistPage(request , num):
	khanande = Singer.objects.get(pk=num)
	ahang_hash = Track.objects.filter(Track_from__id=num)
	ahang_hash_random = list(Track.objects.filter(Track_from__id=num))
	try:
		random_da =  random.choice(ahang_hash_random)
	except:
		random_da = random.choice(list(Track.objects.all()))

	context = {
		'khan': khanande,
		'ahang_hash': ahang_hash,
		'random_player':random_da,
	}
	return render(request, 'music/artist.html', context)

def ListArtistPage(request):
	khanande_ha = Singer.objects.all()
	items = list(Track.objects.all())
	Random_ahang = random.choice(items)
	akhbar = Event.objects.all()[:3]
	context = {
		'khan':khanande_ha,
		'ran':Random_ahang,
		'akhnar':akhbar,
	}
	return render(request, 'music/artists.html', context)

def ContactPage(request):
	items = list(Track.objects.all())
	Random_ahang = random.choice(items)
	context = {
		"ran":Random_ahang,
	}
	return render(request, 'music/contacts.html', context)


def Thankpage(request):
	if request.method == 'POST':
		form_name = request.POST['name']
		form_email = request.POST['email']
		form_subject = request.POST['subject']
		form_text = request.POST['text']
		g = Contact_to_us(name = form_name, email = form_email, subject = form_subject , Message =form_text)
		g.save()
		return render(request, 'feed_back.html')
	else:
		return HttpResponse("<p>ما خودمون ذغال فروشیم دا</p>")

def NewsPage(request):
	khabarha = Event.objects.all()
	items = list(Track.objects.all())
	Random_ahang = random.choice(items)
	context = {
		'khab':khabarha,
		'ran':Random_ahang,
	}
	return render(request, 'music/news.html', context)

def Detail_SongPage(request, nus):
	you = Track.objects.get(pk=nus)
	try:
		me = Album.objects.filter(pk=you.Track_from_Album.id).first()
	except:
		me = None
	comments = Comment.objects.filter(for_Track__id = nus)
	items = list(Track.objects.all())
	Random_ahang = random.choice(items)
	try:
		lot_random_ahang = random.sample(items,4)
	except:
		lot_random_ahang = None
	new_comment = None
	if request.method == 'POST':
		comment_form = CommentForm(data=request.POST)
		if comment_form.is_valid():
			new_comment = comment_form.save(commit=False)
			new_comment.for_track = you
			new_comment.save()

	context = {
		'you':you,
		'me':me,
		'ran':Random_ahang,
		'lot':lot_random_ahang,
		'new_comment': new_comment,
		'comments':comments,
	}
	return render(request, 'music/release.html', context)

def Detail_AlbumPage(request, nuc):
	you = Album.objects.get(pk=nuc)
	me = Track.objects.filter(Track_from_Album__id=nuc)
	items = list(Track.objects.all())
	Random_ahang = random.choice(items)
	lot_random_ahang = random.sample(items,4)
	context = {
		'you':you,
		'me':me,
		'ran':Random_ahang,
		'lot':lot_random_ahang,
	}
	return render(request, 'music/release_album.html', context)

def ReleasesAlbumPage(request):
	album_ha = Album.objects.all()
	items = list(Track.objects.all())
	Random_ahang = random.choice(items)
	akhbar = Event.objects.all()[:3]
	context = {
		'khan':album_ha,
		'ran':Random_ahang,
		'akhnar':akhbar,
	}
	return render(request, 'music/album_ha.html', context)

def ReleasesSongPage(request):
	album_ha = Track.objects.all()
	items = list(Track.objects.all())
	Random_ahang = random.choice(items)
	akhbar = Event.objects.all()[:3]
	context = {
		'khan':album_ha,
		'ran':Random_ahang,
		'akhnar':akhbar,
	}
	return render(request, 'music/track_ha.html', context)

def PrivacyPage(request):
	items = list(Track.objects.all())
	Random_ahang = random.choice(items)
	context = {
		'ran':Random_ahang,
	}
	return render(request, 'music/privacy.html' , context)

def error_404(request, exception):
	return render(request, 'music/404.html')

def ResaultPage(request):
	if request.method == "POST":
		shild = request.POST['user_searched']
		user_singer = Singer.objects.filter(
			Q(name__icontains = shild) | Q(nick_name__icontains = shild) | Q(last_name__icontains = shild)
		)
		user_album = Album.objects.filter(
			Q(name__icontains = shild)
		)
		user_track = Track.objects.filter(
			Q(name__icontains = shild) | Q(desc__icontains = shild) | Q(Time__icontains = shild)
		)
		user_event = Event.objects.filter(
			Q(name__icontains = shild) | Q(short_desc__icontains = shild) | Q(location_Event__icontains = shild) | Q(desc_first__icontains = shild) | Q(end_desc__icontains = shild)
		)

		items = list(Track.objects.all())
		Random_ahang = random.choice(items)

		context = {
			'singer':user_singer,
			'album':user_album,
			'track':user_track,
			'event':user_event,
			'ran':Random_ahang,
		}
		return render(request , 'music/resault.html', context)

	else:
		redirect('music')


@login_required
def PlayListPage(request):
	from_request = request.user
	all_in = Playlist.objects.filter(user=from_request)
	items = list(Track.objects.all())
	Random_ahang = random.choice(items)

	context = {
		'play': all_in,
		'ran':Random_ahang,
	}

	return render(request, 'music/main_playlist.html', context)


@login_required
def PlayListDetailPage(request, num):
	from_request = request.user
	all_in = Playlist.objects.filter(user=from_request, genrate_ran=num)
	all_track = Track.objects.filter(from_playlist__genrate_ran=num)
	items = list(Track.objects.all())
	Random_ahang = random.choice(items)
	lot_random_ahang = random.sample(items,1)
	context = {
		'playing': all_in,
		'play': all_track,
		'ran':Random_ahang,
		'lot':lot_random_ahang,
	}

	return render(request, 'music/detail_playlist.html', context)


def price_lag(request):
	items = list(Track.objects.all())
	Random_ahang = random.choice(items)

	context={
		'random_ahang':Random_ahang,
	}

	return render(request, 'music/pricing.html')


@login_required
@require_common_user
def go_to_gateway_view(request):
	amount = 200000
	factory = bankfactories.BankFactory()
	try:
		bank = factory.create() # or factory.create(bank_models.BankType.BMI) or set identifier
		bank.set_request(request)
		bank.set_amount(amount)
		bank.set_client_callback_url('/music/callback-gateway')    
		bank_record = bank.ready()
		return bank.redirect_gateway()
	except AZBankGatewaysException as e:
		logging.critical(e)
		raise e


def callback_gateway_view(request):
	tracking_code = request.GET.get(settings.TRACKING_CODE_QUERY_PARAM, None)
	if not tracking_code:
		raise Exception()

	try:
		bank_record = bank_models.Bank.objects.get(tracking_code=tracking_code)
	except bank_models.Bank.DoesNotExist:
		raise Exception()

	if bank_record.is_success:
		find_user = Plant.objects.get_or_create(from_user=request.user)
		permission = Permission.objects.get(codename='permium_visit')
		request.user.user_permissions.add(permission)
		return redirect('/music/')
	else:
		return redirect('/music/sub_fail')

def sub_fail_view(request):
	return HttpResponse("پرداخت ناموفق بود   | if you really need it , DM me on Tel --> @something_telegram_accept")
