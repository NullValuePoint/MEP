from django.db import models
from django.utils.encoding import smart_unicode

# Create your models here.

class Announcement(models.Model):
    user_id = models.CharField(max_length=10, null=False, blank=False)
    user_name = models.CharField(max_length=25, null=True, blank=True)
    title = models.CharField(max_length=25, null=False, blank=False)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    text = models.TextField()
    
    def __unicode__(self):
        return smart_unicode(self.title)
    

class Event(models.Model):
    user_id = models.CharField(max_length=10, null=False, blank=False)
    user_name = models.CharField(max_length=25, null=True, blank=True)
    title = models.CharField(max_length=25, null=False, blank=False)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    text = models.TextField()
    
    def __unicode__(self):
        return smart_unicode(self.title)