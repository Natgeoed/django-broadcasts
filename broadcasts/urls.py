# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from .views import get_messages, reset_messages

urlpatterns = patterns(
    '',
    url('^$', get_messages, name="broadcast_messages"),
    url('^reset/$', reset_messages, name="reset_broadcast_messages")
)
