from django.shortcuts import redirect, render, render_to_response, RequestContext
from django.conf import settings
from django.template import RequestContext
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def new_event(request):
    return render_to_response("newannounce.html",
                              locals(),
                              context_instance=RequestContext(request))