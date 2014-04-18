from django import forms
from .models import Announcement

class AnnounceForm(forms.ModelForm):
    class Meta:
        model = Announcement
    
