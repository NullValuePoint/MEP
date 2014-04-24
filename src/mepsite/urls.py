from django.conf.urls import patterns, include, url

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^logout/', 'mepapp.views.logout_view', name='logout'),
    url(r'^about/', 'mepapp.views.about', name='about'),
    url(r'^announcements/', 'mepapp.views.announcement_view', name='announcements'),
    url(r'^new_announcement/', 'mepapp.views.new_announcement_view', name='new_announcement'),
    url(r'^events/', 'mepapp.views.event_view', name='events'),
    url(r'^new_event/', 'mepapp.views.new_event_view', name='new_event'),
    url(r'^scholarships/', 'mepapp.views.scholarship_view', name='scholarships'),
    url(r'^new_scholarship/', 'mepapp.views.new_scholarship_view', name='new_scholarship'),
    url(r'^$', 'mepapp.views.home', name='home'),
    url('', include('social.apps.django_app.urls', namespace='social')),
    
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)