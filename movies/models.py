# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Movies(models.Model):
    movie_name = models.CharField(max_length=250)
    genre = models.CharField(max_length=250)
    number_of_awards = models.CharField(max_length=250)
    time_of_movie = models.CharField(max_length=250) ### is that a problem int-str association
    director = models.CharField(max_length=250)
    scenarist = models.CharField(max_length=250)
    def __str__(self):
        return self.movie_name + " " + self.time_of_movie + " " + self.director

class Movie_star(models.Model):
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    age = models.CharField(max_length=250)
    height = models.CharField(max_length=250)
    def __str__(self):
        return self.name



