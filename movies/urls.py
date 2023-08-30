from django.contrib import admin
from django.urls import path
from django.urls import include, path
from . import views
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('movies', views.MoviesViewSet, basename='movies')

urlpatterns = router.urls

