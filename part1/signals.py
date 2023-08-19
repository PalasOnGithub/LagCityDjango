

"""
@receiver(user_logged_in)
def post_login(sender, user, request, **kwargs):
    try:
        fot_user = Plant.objects.get(from_user__id=user.pk)
        hi = time.time() // 1
        hello = fot_user.start_from_timing // 1
        if hi - hello:
            pass

    except:
        
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        instance.objects.update(finish_from_timing=str(time.time() + 2592000))

"""