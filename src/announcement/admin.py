from django.contrib import admin

# Register your models here.
from .models import Announcement

class AnnouncementAdmin(admin.ModelAdmin):
    class Meta:
        model = Announcement
    
admin.site.register(Announcement, AnnouncementAdmin)