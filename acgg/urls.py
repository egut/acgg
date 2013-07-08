from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'acgg.views.home', name='home'),
    # url(r'^acgg/', include('acgg.foo.urls')),

    #Django allauth
    (r'^accounts/', include('allauth.urls')),
    # url(r'^$', TemplateView.as_view(template_name='index.html')),
	url(r'^accounts/profile/$', TemplateView.as_view(template_name='profile.html')),

	#Django Avatar
	(r'^avatar/', include('avatar.urls')),	

    #Django Smart Selectors
    url(r'^chaining/', include('smart_selects.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    
    #Need to be last
    url(r'^', include('cms.urls')),
)


if settings.DEBUG:
    urlpatterns = patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    url(r'', include('django.contrib.staticfiles.urls')),
) + urlpatterns