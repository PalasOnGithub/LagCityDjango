from .models import Comment
from django import forms
from .models import*

"""
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name','email','body')

# The fields need to add!
"""
"""
class PlayListForm(forms.Form):
    NamePL = forms.CharField(max_length=100)
    SongsPL = forms.MultipleChoiceField(Track, required=False)
    ImagePL = forms.ImageField(upload_to= 'Picture/User_PlayList/%Y/%m/%d/', required=False)



            if find_user.finish_from_timing - datetime.today() > 0:
            time.sleep(1)
        else:
            find_user.delete()
            permission = Permission.objects.filter(codename='permium_visit').first()
            request.user.user_permissions.delete(permission)
    except:

"""