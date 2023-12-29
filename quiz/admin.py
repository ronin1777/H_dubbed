from django.contrib import admin

import nested_admin

from quiz.models import Answer, Question, UsersAnswer


# Register your models here.


class AnswerInline(nested_admin.NestedTabularInline):
    model = Answer
    extra = 4
    max_num = 4


class QuestionInline(nested_admin.NestedTabularInline):
    model = Question
    inlines = [AnswerInline,]
    extra = 4


class QuizAdmin(nested_admin.NestedModelAdmin):
    inlines = [QuestionInline]


class UserAnswerInline(admin.TabularInline):
    model = UsersAnswer
