from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from badge.models import Badge
from badge.serializers import BadgeSerializer
from movies.permisions import IsAdminOrReadOnly


class BadgeView(ListCreateAPIView):
    serializer_class = BadgeSerializer
    queryset = Badge.objects.all()
    permission_classes = [IsAdminOrReadOnly]


class BadgeUpdateView(RetrieveUpdateDestroyAPIView):
    serializer_class = BadgeSerializer
    queryset = Badge.objects.all()
    permission_classes = [IsAdminOrReadOnly]

