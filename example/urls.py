# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.conf import settings
from django.contrib import admin

admin.autodiscover()


urlpatterns = [
    url(r'^messages/', include('broadcasts.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('simpleapp.urls')),
    ]

urlpatterns += [
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),
    ] if settings.DEBUG else urlpatterns
