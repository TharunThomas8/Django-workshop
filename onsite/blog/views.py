# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import ListView
from . import models


# Create your views here.

class HomePageView(ListView):
    model = models.Post
    template_name = 'blog/blog_post.html'
