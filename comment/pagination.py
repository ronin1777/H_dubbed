from rest_framework.pagination import PageNumberPagination


class CommentPagination(PageNumberPagination):
    page_size = 10


class PostPagination(PageNumberPagination):
    page_size = 5
