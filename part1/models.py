from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from random import randint
from datetime import datetime, timedelta


def get_deadline():
    return datetime.today() + timedelta(days=30)


class Sabk(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    picture = models.ImageField(upload_to= 'Picture/Sabk_pictures/%Y/%m/%d/',null=True, blank=True)
    desc = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Singer(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True )
    nick_name = models.CharField(max_length=50, null=True , blank = True)
    last_name = models.CharField(max_length=50, null=True , blank = True)
    picture = models.ImageField(upload_to='Picture/singers_picture/%Y/%m/%d/',null=True, blank=True)
    age = models.IntegerField(null=True, blank=True )
    Style = models.ForeignKey(Sabk , on_delete=models.CASCADE, null=True, blank=True )
    desc = models.TextField(null=True, blank=True)
    create_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail_artist', args=[str(self.id)])


class Album(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True )
    desc = models.TextField(null=True, blank=True)
    Album_from = models.ForeignKey(Singer , on_delete = models.CASCADE, null=True, blank=True )
    Album_sabk = models.ForeignKey(Sabk , on_delete = models.CASCADE, null=True, blank=True )
    picture = models.ImageField(upload_to= 'Picture/Album_pictures/%Y/%m/%d/',null=True, blank=True)
    create_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.name 

    def get_absolute_url(self):
        return reverse('detail_album', args=[str(self.id)])

class Playlist(models.Model):
    list_name=models.CharField(max_length=100)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    picture = models.ImageField(upload_to= 'Picture/User_PlayList/%Y/%m/%d/',null=True, blank=True)
    create_on = models.DateTimeField(auto_now_add=True)
    desc = models.TextField(null=True, blank=True)
    genrate_ran = models.IntegerField(null=False, blank=False,default=randint(10000, 2765000), editable=False)
    pub_son = models.ManyToManyField('Track' , null = True , blank = True)

    def __str__(self):
        return self.list_name

    def get_absolute_url(self):
        return reverse('detail_playlist', args=[str(self.genrate_ran)])


class Track(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True )
    desc = models.TextField(null=True, blank=True)
    Track_from = models.ForeignKey(Singer , on_delete = models.CASCADE, null=True, blank=True )
    Track_sabk = models.ForeignKey(Sabk , on_delete = models.CASCADE, null=True, blank=True )
    Track_from_Album = models.ForeignKey(Album , on_delete = models.CASCADE, null=True, blank=True )
    picture = models.ImageField(upload_to= 'Picture/Track_pictures/%Y/%m/%d/',null=True, blank=True)
    track_audio = models.FileField(upload_to = 'Audios/%Y/%m/%d/', null=True, blank=True )
    track_audio_remix = models.FileField(upload_to = 'Audios/Remixes/%Y/%m/%d/' , null = True , blank = True)
    likes = models.ManyToManyField(User, related_name= 'Track_like' , null=True , blank=True)
    Time = models.CharField(max_length = 10, null=True ,blank=True)
    create_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail_song', args=[str(self.id)])


    class Meta:
        permissions = [
            ("permium_visit", "can see the permium tracks"),
        ]


class Comment(models.Model):
    for_Track = models.ForeignKey(Track, on_delete = models.CASCADE, null=True, blank=True )
    name = models.CharField(max_length = 70, null=True, blank=True )
    email = models.EmailField( null=True, blank=True )
    body = models.TextField( null=True, blank=True )
    create_on = models.DateTimeField(auto_now_add = True)
    active = models.BooleanField(default = False)

    class Meta:
        ordering = ['create_on']

    def __str__(self):
        return 'comment {} by {}'.format(self.body, self.name)


class Event(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True )
    short_desc = models.TextField( null=True, blank=True )
    location_Event = models.TextField(null = True , blank = True)
    desc_first = models.TextField( null=True, blank=True )
    propert_1 = models.CharField(max_length = 100)
    propert_2 = models.CharField(max_length = 100, null=True , blank=True)
    propert_3 = models.CharField(max_length = 100, null=True , blank=True)
    propert_4 = models.CharField(max_length = 100, null=True , blank=True)
    propert_5 = models.CharField(max_length = 100, null=True , blank=True)
    propert_6 = models.CharField(max_length = 100, null=True , blank=True)
    propert_8 = models.CharField(max_length = 100, null=True , blank=True)
    propert_9 = models.CharField(max_length = 100, null=True , blank=True)
    propert_10 = models.CharField(max_length = 100, null=True , blank=True)
    picture = models.ImageField(upload_to= 'Picture/Event_pictures/%Y/%m/%d/',null=True, blank=True)
    end_desc = models.TextField(null = True, blank= True)
    video = models.FileField(upload_to = 'Audios/%Y/%m/%d/', null=True , blank = True)
    create_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail_new', args=[str(self.id)])



class Contact_to_us(models.Model):
    name = models.CharField(max_length=50, null = True, blank = True)
    email = models.EmailField(max_length=254, null = True, blank = True)
    subject = models.CharField(max_length=50, null = True, blank = True)
    Message = models.TextField(null = True, blank = True)

    def __str__(self):
        return self.name

#    def get_deadline():
 #      return datetime.today() + timedelta(days=30)


class Plant(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_from = models.DateTimeField(auto_now_add=True)
    ended = models.BooleanField(default=True)
    finish_from_timing = models.DateField(default=get_deadline)

    def __str__(self):
        return self.from_user.username + "   -- >   " +str(self.finish_from_timing)


class HomeBack(models.Model):
    name = models.TextField()
    picture = models.ImageField(upload_to= 'Picture/Home_main_image/',null=True, blank=True)

