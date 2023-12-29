from django.urls import path, re_path
from .views import MyQuizListAPI, QuizListAPI, QuizTakerCreateView

app_name = 'quiz'
urlpatterns = [
    path("my-quizzes/", MyQuizListAPI.as_view()),
    path("nowquizzes/", QuizTakerCreateView.as_view()),
    path("quizzes/", QuizListAPI.as_view()),

]
