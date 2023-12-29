from rest_framework import serializers

from quiz.models import Category, Quiz, Answer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title', 'quiz_count']


class QuizListSerializer(serializers.ModelSerializer):
    questions_count = serializers.SerializerMethodField()

    class Meta:
        model = Quiz
        fields = ["id", "title", "slug", "questions_count"]
        read_only_fields = ["questions_count"]

    def get_questions_count(self, obj):
        return obj.question_set.all().count()


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ["id", "question", "title"]






















































