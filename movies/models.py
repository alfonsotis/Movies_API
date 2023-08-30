from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=255)


class Movie(models.Model):
    title = models.TextField(null=False)
    description = models.TextField(null=False)
    genres = models.ManyToManyField(Genre)
    release_date = models.DateField()
    vote_average = models.DecimalField(max_digits=3, decimal_places=1)
    vote_count = models.IntegerField()
