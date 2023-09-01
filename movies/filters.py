from django_filters.rest_framework import FilterSet

from .models import Movie

class MovieFilter(FilterSet):
    class Meta:
        model = Movie
        fields = {
            'genres__name': ['exact'],
            'vote_average': ['exact'],
            'release_date': ['gt','lt'],
        }