# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Movies, Movie_star



# Register your models here.
admin.site.register(Movies)
admin.site.register(Movie_star)