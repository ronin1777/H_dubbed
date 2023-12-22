from django.urls import path
from .views import *

app_name = 'movie'

urlpatterns = [
    path('createmovie/', MovieCreateView.as_view()),

]
