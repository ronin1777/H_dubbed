from django.db import models

from h_dubbed import settings


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Quiz(models.Model):
    title = models.CharField(max_length=300)
    cat = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    slug = models.SlugField(max_length=50, blank=True)
    is_Active = models.BooleanField(default=True)
    score_required = models.PositiveSmallIntegerField(default=60)
    time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['time', ]
        verbose_name_plural = 'Quizzes'

    def __str__(self):
        return self.title

    @property
    def question_count(self):
        return self.question_set.count()


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)

    def __str__(self):
        return self.title


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=True, blank=True)
    is_right = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class QuizTaker(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    score = models.PositiveSmallIntegerField(default=0)
    completed = models.BooleanField(default=False)
    is_passed = models.BooleanField(default=False)
    time = models.DateTimeField(auto_now_add=True)
    date_completed = models.DateTimeField(default=None, null=True, blank=True)

    def __str__(self):
        return self.user.email


class UsersAnswer(models.Model):
    quiz_taker = models.ForeignKey(QuizTaker, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, null=True, blank=True)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)

    def __str__(self):
        return self.question.title













































