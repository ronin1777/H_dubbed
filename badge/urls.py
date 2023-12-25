from django.urls import path, include

from .views import *

app_name = 'badge'

urlpatterns = [
    path('badge/', BadgeView.as_view()),
    path('badgeupdate/<int:pk>/', BadgeUpdateView.as_view()),

]
