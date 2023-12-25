from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from badge.models import Badge, UserBadge
from badge.serializers import BadgeSerializer, UserBadgeSerializer
from movies.permisions import IsAdminOrReadOnly


class BadgeView(ListCreateAPIView):
    serializer_class = BadgeSerializer
    queryset = Badge.objects.all()
    permission_classes = [IsAdminOrReadOnly]


class BadgeUpdateView(RetrieveUpdateDestroyAPIView):
    serializer_class = BadgeSerializer
    queryset = Badge.objects.all()
    permission_classes = [IsAdminOrReadOnly]


class UserBadgeProgressView(generics.RetrieveAPIView):
    serializer_class = UserBadgeSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'badge_id'

    def get_queryset(self):
        user = self.request.user
        badge_id = self.kwargs['badge_id']
        return UserBadge.objects.filter(user=user, badge_id=badge_id)
