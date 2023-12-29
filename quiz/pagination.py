from rest_framework.pagination import PageNumberPagination


class QuizTaker(PageNumberPagination):
    page_size = 1


class QuizList(PageNumberPagination):
    page_size = 5
