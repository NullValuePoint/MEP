from django.shortcuts import redirect, render, render_to_response, RequestContext
from django.conf import settings
from django.template import RequestContext
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def new(request):
    return render_to_response("newannounce.html",
                              locals(),
                              context_instance=RequestContext(request))


def announcement(request):
    return render_to_response("announcements.html",
                              locals(),
                              context_instance=RequestContext(request))
