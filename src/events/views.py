from django.shortcuts import redirect, render, render_to_response, RequestContext
from django.conf import settings
from django.template import RequestContext
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def new_event_view(request):
    return render_to_response("newevent.html",
                              locals(),
                              context_instance=RequestContext(request))


def event_view(request):
    return render_to_response("events.html",
                              locals(),
                              context_instance=RequestContext(request))