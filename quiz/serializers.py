from rest_framework import serializers

from quiz.models import Category, Quiz, Answer, Question, UsersAnswer, QuizTaker


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


class QuestionSerializer(serializers.ModelSerializer):
    answer_set = AnswerSerializer(many=True)

    class Meta:
        model = Question
        fields = "__all__"


class UsersAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsersAnswer
        fields = "__all__"


# class QuizResultSerializers(serializers.ModelSerializer):
#     completed = serializers.SerializerMethodField()
#     progress = serializers.SerializerMethodField()
#     questions_count = serializers.SerializerMethodField()
#     score = serializers.SerializerMethodField()
#     is_passed = serializers.SerializerMethodField()
#
#     class Meta:
#         model = Quiz
#         fields = ["id", "title", "slug", "questions_count", "completed", "score", "progress", 'score_required', 'is_passed']
#         read_only_fields = ["questions_count", "completed", "progress"]
#
#     def get_completed(self, obj):
#         try:
#             quiztaker = QuizTaker.objects.get(user=self.context['request'].user, quiz=obj)
#             questions_answered = UsersAnswer.objects.filter(quiz_taker=quiztaker, answer__isnull=False).count()
#             total_questions = obj.question_count
#             if questions_answered == total_questions:
#                 quiztaker.completed = True
#                 return quiztaker.completed
#             else:
#                 return False
#         except QuizTaker.DoesNotExist:
#             return None
#
#     def get_progress(self, obj):
#         try:
#             quiztaker = QuizTaker.objects.get(user=self.context['request'].user, quiz=obj)
#             if not quiztaker.completed:
#                 questions_answered = UsersAnswer.objects.filter(quiz_taker=quiztaker, answer__isnull=False).count()
#                 total_questions = obj.question_count
#                 progress = (questions_answered / total_questions) * 100
#                 return round(progress, 2)
#             return None
#         except QuizTaker.DoesNotExist:
#             return None
#
#     def get_questions_count(self, obj):
#         return obj.question_count
#
#     def get_score(self, obj):
#         answer_user = obj.usersanswer_set.filter(answer__is_right=True).count()
#         total_question = obj.question_set.count()
#         score = (answer_user / total_question) * 100
#         return round(score, 2)
#
#     def get_is_passed(self, obj):
#         answer_user = obj.usersanswer_set.filter(answer__is_right=True).count()
#         total_question = obj.question_set.count()
#         score = (answer_user / total_question) * 100
#         if score and score >= obj.score_required:
#             return True
#         else:
#             return False


class QuizTakerSerializer(serializers.ModelSerializer):
    users_answer = UsersAnswerSerializer(many=True)

    score = serializers.SerializerMethodField()
    is_passed = serializers.SerializerMethodField()

    class Meta:
        model = QuizTaker
        fields = ['id', 'user', 'quiz', 'score', 'completed', 'is_passed', 'users_answer']
        read_only = ['user', 'quiz', 'score', 'completed', 'is_passed']

    def get_score(self, obj):
        total_questions = obj.quiz.question_set.count()
        correct_answers = obj.usersanswer_set.filter(answer__is_right=True).count()
        score = (correct_answers / total_questions) * 100
        return round(score, 2)

    def get_is_passed(self, obj):
        if obj.score >= obj.quiz.score_required:
            return True


class ResultSerializers(serializers.ModelSerializer):
    class Meta:
        model = QuizTaker
        fields = ('user', 'quiz', 'score', 'completed', 'is_passed', )










































