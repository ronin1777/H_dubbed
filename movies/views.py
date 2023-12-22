from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from movies.filters import MovieFilters
from movies.models import Movie
from movies.permisions import IsAdminOrReadOnly
from movies.serializers import MovieSerializers


class MovieCreateView(ListCreateAPIView):
    permission_classes = [IsAdminOrReadOnly]
    queryset = Movie.objects.all()
    serializer_class = MovieSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_class = MovieFilters


class MovieUpdateView(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializers
    permission_classes = [IsAdminOrReadOnly]


class MovieSearch(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializers
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']
