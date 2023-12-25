from django.urls import path

from comment.views.admin import PostCreateViewSet, PostUpdateView
from comment.views.client import CommentViewSet, CommentRetrieveUpdateDeleteView, PostListViewSet

app_name = 'post'
urlpatterns = [
    path('list_post/', PostListViewSet.as_view(), name='list_post'),
    path('comment/', CommentViewSet.as_view(), name='comment'),
    path('update_comment/<int:pk>/', CommentRetrieveUpdateDeleteView.as_view(), name='comment'),

    #admin urls

    path('create_post/', PostCreateViewSet.as_view(), name='create_post'),
    path('update_post/<int:pk>/', PostUpdateView.as_view(), name='update_post'),

]
