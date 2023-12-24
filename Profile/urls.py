from django.urls import path, include
from rest_framework import routers
from Profile import views
app_name = 'profile'

router = routers.DefaultRouter()
router.register('', views.ProfileViewSet, basename='Profile')

urlpatterns = [

]
urlpatterns += router.urls
