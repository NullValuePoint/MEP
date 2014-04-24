from django.shortcuts import redirect, render, render_to_response, RequestContext
from django.conf import settings
from django.template import RequestContext
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
#from social.backends.linkedin import LinkedinOAuth2
#from social.apps.django_app.default.models import UserSocialAuth


def home(request):
    
    #scope = ''.join(settings.SOCIAL_AUTH_LINKEDIN_OAUTH2_SCOPE)
    #social_user = UserSocialAuth.objects.get(user_id=request.user.id)
    
    # print type(social_user.extra_data)
    # print social_user.extra_data
    
    return render_to_response("home.html", {
                                #'user': request.user,
                                #'extra_data': social_user.extra_data,
                                'linkedin_id': getattr(settings, 'SOCIAL_AUTH_LINKEDIN_OAUTH2_KEY', None),
                                #'linkedin_scope': scope
                                },
                              context_instance=RequestContext(request))


@login_required
def logout_view(request):
    logout(request)
    return render_to_response("home.html",
                              locals(),
                              context_instance=RequestContext(request))


def about(request):
    return render_to_response("about.html",
                              locals(),
                              context_instance=RequestContext(request))