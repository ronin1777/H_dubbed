from django.shortcuts import render
from rest_framework import generics, permissions

from quiz.models import Quiz
from quiz.serializers import QuizResultSerializers, QuizListSerializer


# Create your views here.
class MyQuizListAPI(generics.ListAPIView):
    """
    Quizzes for each user.
    In this endpoint, users can view the quizzes they have completed.
    """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = QuizResultSerializers

    def get_queryset(self, *args, **kwargs):
        queryset = Quiz.objects.filter(quiztaker__user=self.request.user)
        return queryset


class QuizListAPI(generics.ListAPIView):
    """
    Users can see all quizzes except the ones they have answered.
    """
    serializer_class = QuizListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self, *args, **kwargs):
        queryset = Quiz.objects.filter(is_Active=True).exclude(quiztaker__user=self.request.user)
        return queryset