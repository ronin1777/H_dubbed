from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from movies.filters import MovieFilters
from movies.models import Movie
from movies.serializers import MovieSerializers


class MovieCreateView(ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_class = MovieFilters


class MovieUpdateView(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializers

