from django.urls import path, include


from media.views import MediaCreateListView, MediaUpdateView

app_name = 'media'

urlpatterns = [


    path('media/', MediaCreateListView.as_view(), name='media_upload'),
    path('media/<int:pk>', MediaUpdateView.as_view(), name='media_update'),

]


