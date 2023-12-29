from rest_framework import serializers

from quiz.models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title', 'quiz_count']
