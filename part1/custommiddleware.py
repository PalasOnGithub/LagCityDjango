from datetime import datetime
from .models import Plant, Track
from django.contrib.auth.models import Permission


class checksub:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            find_user = Plant.objects.get(from_user=request.user)
            uptio = request.user
            if find_user.finish_from_timing == datetime.today():
                #print("yes expired! kick him out of system")
                permission_user = Permission.objects.get(codename='permium_visit')
                uptio.user_permissions.remove(permission_user)
                find_user.delete()
            else:
                pass
                #print("not expired")
        except:
            pass
        
        response = self.get_response(request)

        return response
