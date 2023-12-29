from django.urls import path

from level.views import CreateLevel, UpdateLevel

app_name = 'Level'

urlpatterns = [
   path('create_level/', CreateLevel.as_view(), name='create_level'),
   path('update_level/<int:pk>', UpdateLevel.as_view(), name='update_level'),
]
