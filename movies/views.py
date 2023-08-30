from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter

from movies.filters import MovieFilter
from .models import Movie
from .serializers import MoviesSerializer


class MoviesViewSet(ModelViewSet):
    http_method_names = ['get', 'put', 'delete', 'post']
    queryset = Movie.objects.prefetch_related('genres').all()
    serializer_class = MoviesSerializer
    pagination_class = PageNumberPagination
    filter_backends = [SearchFilter, DjangoFilterBackend]

    search_fields = ['title', 'description']
    # filterset_fields = ['title', 'description', 'genres__name', 'vote_average', 'release_date']
    filterset_class = MovieFilter
    search_param = ['exact']
