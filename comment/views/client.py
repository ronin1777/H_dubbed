from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView

from comment.models import Post, Comment
from comment.serializers import PostSerializer, CommentSerializer
from rest_framework import filters


class PostListViewSet(ListAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    filter_backends = [filters.SearchFilter]
    search_fields = ['title']


class CommentViewSet(ListCreateAPIView):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
