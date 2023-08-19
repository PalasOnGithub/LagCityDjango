from django.contrib import admin
from .models import*

admin.site.register(Sabk)
admin.site.register(Singer)
admin.site.register(Album)
admin.site.register(Track)
admin.site.register(Event)
admin.site.register(Comment)
admin.site.register(Contact_to_us)
admin.site.register(Playlist)
admin.site.register(Plant)
admin.site.register(HomeBack)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name','body','for_Track','created_on','active')
    list_filter = ('active','create_on')
    search_fields = ('name','email','body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)
