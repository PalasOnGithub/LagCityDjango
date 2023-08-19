from django.db import models
from django.urls import reverse
# Create your models here.

class Platform(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True, verbose_name="اسم")
    picture = models.ImageField(upload_to= 'Picture/game/Platform_pictures/%Y/%m/%d/',null=True, blank=True, verbose_name="عکس")
    desc = models.TextField(null=True, blank=True, verbose_name='توضیحات')

    def __str__(self):
        return self.name

class Sabk(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    picture = models.ImageField(upload_to= 'game/Picture/Sabk_pictures/%Y/%m/%d/',null=True, blank=True)
    desc = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


GEEKS_CHOICES =(
    ("1", "یک ستاره"),
    ("2", "دو ستاره"),
    ("3", "سه ستاره"),
    ("4", "چهار ستاره"),
    ("5", "پنج ستاره"),
)

class Game(models.Model):
    from_platform = models.ForeignKey(Platform, on_delete=models.CASCADE)
    from_sabk = models.ForeignKey(Sabk, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True, blank=True, verbose_name="اسم")
    create_on = models.DateTimeField(auto_now_add=True)
    score = models.CharField(max_length= 20,choices = GEEKS_CHOICES, verbose_name = "امتیاز")
    download_from_google = models.TextField(null=True , blank = True, verbose_name="دانلود از گوگل")
    req = models.TextField(null=True , blank = True, verbose_name="مورد نیاز سیستم")
    action_box = models.TextField(null=True , blank = True, verbose_name="اکشن")
    effect_box = models.TextField(null=True , blank = True, verbose_name="افکت")
    online_box = models.TextField(null=True , blank = True, verbose_name="انلاین گیم")
    animation_box = models.TextField(null=True , blank = True, verbose_name="انیمیشن")
    desc = models.TextField(null=True, blank = True, verbose_name="اطلاعات")
    short_desc = models.TextField(null=True, blank = True, verbose_name="اطلاعات کمتر")
    how_to_install = models.TextField(null = True , blank = True , verbose_name= "راهنمای نصب")
    sim_1 = models.CharField(max_length= 220, null = True , blank = True , verbose_name="امتیاز")
    sim_2 = models.CharField(max_length= 220, null = True , blank = True , verbose_name="امتیاز")
    sim_3 = models.CharField(max_length= 220, null = True , blank = True , verbose_name="امتیاز")
    sim_4 = models.CharField(max_length= 220, null = True , blank = True , verbose_name="امتیاز")
    sim_5 = models.CharField(max_length= 220, null = True , blank = True , verbose_name="امتیاز")
    video = models.FileField(upload_to = 'game/videos/%Y/%m/%d/' , null = True , blank = True, verbose_name="تریلر")
    pic = models.ImageField(upload_to = 'game/pictures/%Y/%m/%d/' , null = True , blank = True, verbose_name="عکس")
    download_1 = models.CharField(max_length= 320, null = True , blank = True , verbose_name="لینک دانلود")
    download_2 = models.CharField(max_length= 320, null = True , blank = True , verbose_name="لینک دانلود")
    download_3 = models.CharField(max_length= 320, null = True , blank = True , verbose_name="لینک دانلود")
    download_4 = models.CharField(max_length= 320, null = True , blank = True , verbose_name="لینک دانلود")
    download_5 = models.CharField(max_length= 320, null = True , blank = True , verbose_name="لینک دانلود")
    download_6 = models.CharField(max_length= 320, null = True , blank = True , verbose_name="لینک دانلود")
    download_7 = models.CharField(max_length= 320, null = True , blank = True , verbose_name="لینک دانلود")
    download_8 = models.CharField(max_length= 320, null = True , blank = True , verbose_name="لینک دانلود")
    download_9 = models.CharField(max_length= 320, null = True , blank = True , verbose_name="لینک دانلود")
    download_10 = models.CharField(max_length= 320, null = True , blank = True , verbose_name="لینک دانلود")
    download_11 = models.CharField(max_length= 320, null = True , blank = True , verbose_name="لینک دانلود")
    download_12 = models.CharField(max_length= 320, null = True , blank = True , verbose_name="لینک دانلود")
    download_13 = models.CharField(max_length= 320, null = True , blank = True , verbose_name="لینک دانلود")
    download_14 = models.CharField(max_length= 320, null = True , blank = True , verbose_name="لینک دانلود")
    download_15 = models.CharField(max_length= 320, null = True , blank = True , verbose_name="لینک دانلود")
    hajm_1 = models.CharField(max_length= 320, null = True , blank = True , verbose_name="حجم پارت 1")
    hajm_2 = models.CharField(max_length= 320, null = True , blank = True , verbose_name="حجم پارت 2")
    hajm_3 = models.CharField(max_length= 320, null = True , blank = True , verbose_name="حجم پارت 3")
    hajm_4 = models.CharField(max_length= 320, null = True , blank = True , verbose_name="حجم پارت 4")
    hajm_5 = models.CharField(max_length= 320, null = True , blank = True , verbose_name="حجم پارت 5")
    hajm_6 = models.CharField(max_length= 320, null = True , blank = True , verbose_name="حجم پارت 6")
    hajm_7 = models.CharField(max_length= 320, null = True , blank = True , verbose_name="حجم پارت 7")
    hajm_8 = models.CharField(max_length= 320, null = True , blank = True , verbose_name="حجم پارت 8")
    hajm_9 = models.CharField(max_length= 320, null = True , blank = True , verbose_name="حجم پارت 9")
    hajm_10 = models.CharField(max_length= 320, null = True , blank = True , verbose_name="حجم پارت 10")
    hajm_11 = models.CharField(max_length= 320, null = True , blank = True , verbose_name="حجم پارت 11")
    hajm_12 = models.CharField(max_length= 320, null = True , blank = True , verbose_name="حجم پارت 12")
    hajm_13 = models.CharField(max_length= 320, null = True , blank = True , verbose_name="حجم پارت 13")
    hajm_14 = models.CharField(max_length= 320, null = True , blank = True , verbose_name="حجم پارت 14")
    hajm_14 = models.CharField(max_length= 320, null = True , blank = True , verbose_name="حجم پارت 15")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail_game', args=[str(self.id)])


class Mosabghe(models.Model):
    from_platform = models.ForeignKey(Platform, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True, blank=True, verbose_name="اسم")
    create_on = models.DateTimeField(auto_now_add=True)
    req = models.TextField(null=True , blank = True, verbose_name="مورد نیاز اطلاعات")
    desc = models.TextField(null=True, blank = True, verbose_name="اطلاعات")
    video = models.FileField(upload_to = 'game/mosabghe/videos/%Y/%m/%d/' , null = True , blank = True, verbose_name="تریلر")
    pic = models.ImageField(upload_to = 'game/mosabghe/pictures/%Y/%m/%d/' , null = True , blank = True, verbose_name="عکس")

    def __str__(self):
        return self.name


class News(models.Model):
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
    create_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail_blog', args=[str(self.id)])



class Comment(models.Model):
    for_Track = models.ForeignKey(News, on_delete = models.CASCADE, null=True, blank=True )
    name = models.CharField(max_length = 70, null=True, blank=True )
    email = models.EmailField( null=True, blank=True )
    body = models.TextField( null=True, blank=True )
    create_on = models.DateTimeField(auto_now_add = True)
    active = models.BooleanField(default = False)

    class Meta:
        ordering = ['create_on']

    def __str__(self):
        return 'comment {} by {}'.format(self.body, self.name)

class Contact_to_us(models.Model):
    name = models.CharField(max_length=50, null = True, blank = True)
    email = models.EmailField(max_length=254, null = True, blank = True)
    subject = models.CharField(max_length=50, null = True, blank = True)
    Message = models.TextField(null = True, blank = True)

    def __str__(self):
        return self.name
