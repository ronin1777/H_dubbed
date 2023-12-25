from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from comment.models import Post, Comment
from comment.serializers import PostSerializer, CommentSerializer
from rest_framework import filters, status
from comment.tasks import assign_badge


class PostListViewSet(ListAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    filter_backends = [filters.SearchFilter]
    search_fields = ['title']


class CommentViewSet(ListCreateAPIView):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        comment = serializer.save()
        user = comment.user
        assign_badge.delay(user.id)


class CommentRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
