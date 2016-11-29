# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.views.generic import ListView, DetailView

from .models import SimpleModel


urlpatterns = [
    url(r'^$', ListView.as_view(model=SimpleModel), name="simplemodel_list"),
    url(r'^(?P<slug>[\w-]+)/', DetailView.as_view(model=SimpleModel),
        name='simplemodel_detail'),
    ]
