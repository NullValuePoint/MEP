from django.shortcuts import redirect, render, render_to_response, RequestContext
from django.conf import settings
from django.template import RequestContext
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
           
    return render_to_response("home.html",
                              {'linkedin_id': getattr(settings, 'SOCIAL_AUTH_LINKEDIN_KEY', None)},
                              context_instance=RequestContext(request))


def logout_view(request):
    logout(request)
    return render_to_response("home.html",
                              {},
                              context_instance=RequestContext(request))