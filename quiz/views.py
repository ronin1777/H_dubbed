from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from quiz.models import Quiz, QuizTaker
from quiz.serializers import QuizListSerializer, QuizTakerSerializer, ResultSerializers


# Create your views here.
class MyQuizListAPI(generics.ListAPIView):
    """
    Quizzes for each user.
    In this endpoint, users can view the quizzes they have completed.
    """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ResultSerializers

    def get_queryset(self, *args, **kwargs):
        queryset = QuizTaker.objects.filter(user=self.request.user)
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


class QuizTakerCreateView(CreateAPIView):
    serializer_class = QuizTakerSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.calculate_progres()
        instance.save()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


















