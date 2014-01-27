# -*- coding: utf-8 -*-
from django.conf.urls import url, patterns

from .models import SimpleModel
from django.views.generic import ListView, DetailView

urlpatterns = patterns(
    '',
    url(r'^$',
        ListView.as_view(model=SimpleModel),
        name="simplemodel_list"
    ),
    url(r'^(?P<slug>[\w-]+)/',
        DetailView.as_view(model=SimpleModel),
        name='simplemodel_detail',
    ),
)
