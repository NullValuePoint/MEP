from django.db import models
from django.utils.encoding import smart_unicode

# Create your models here.

class Announcement(models.Model):
    announcer_id = models.CharField(max_length=10, null=False, blank=False)
    announcer_name = models.CharField(max_length=25, null=True, blank=True)
    announcement_title = models.CharField(max_length=25, null=False, blank=False)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    announcement_text = models.TextField()
    
    def __unicode__(self):
        return smart_unicode(self.announcement_title)
    