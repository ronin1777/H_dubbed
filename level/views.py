from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from level.models import Level
from level.serializers import LevelSerializers
from movies.permisions import IsAdminOrReadOnly


# Create your views here.


class CreateLevel(ListCreateAPIView):
    serializer_class = LevelSerializers
    queryset = Level.objects.all()
    permission_classes = [IsAdminOrReadOnly]


class UpdateLevel(RetrieveUpdateDestroyAPIView):
    serializer_class = LevelSerializers
    queryset = Level.objects.all()
    permission_classes = [IsAdminOrReadOnly]
