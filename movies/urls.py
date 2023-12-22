from django.urls import path
from .views import *

app_name = 'movie'

urlpatterns = [
    path('createmovie/', MovieCreateView.as_view()),
    path('updatemovie/<int:pk>/', MovieUpdateView.as_view()),
    path('movie_search/', MovieSearch.as_view()),
]
