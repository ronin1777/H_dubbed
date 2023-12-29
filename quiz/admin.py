from django.contrib import admin

import nested_admin

from quiz.models import Answer


# Register your models here.


class AnswerInline(nested_admin.NestedTabularInline):
    model = Answer
    extra = 4
    max_num = 4
