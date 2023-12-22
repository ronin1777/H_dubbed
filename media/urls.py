from django.urls import path, include


from media.views import MediaCreateListView, MediaUpdateView, BucketHome, DeleteBucketObject, DownloadBucketObject

app_name = 'media'

urlpatterns = [


    path('media/', MediaCreateListView.as_view(), name='media_upload'),
    path('media/<int:pk>', MediaUpdateView.as_view(), name='media_update'),

    path('bucket/', BucketHome.as_view(), name='bucket-home'),
    path('bucket/delete/<str:key>/', DeleteBucketObject.as_view(), name='bucket-delete'),
    path('bucket/download/<str:key>/', DownloadBucketObject.as_view(), name='bucket-download'),

]


