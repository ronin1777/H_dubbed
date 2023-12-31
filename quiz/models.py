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

    @property
    def answer_count(self):
        return self.answer_set.count()


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=True, blank=True)
    is_right = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class QuizTaker(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_quiz')
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    score = models.PositiveSmallIntegerField(default=0)
    completed = models.BooleanField(default=False)
    is_passed = models.BooleanField(default=False)
    time = models.DateTimeField(auto_now_add=True)
    date_completed = models.DateTimeField(default=None, null=True, blank=True)

    def __str__(self):
        return self.user.email

    def save(self, *args, **kwargs):
        is_new_instance = not self.pk
        self.calculate_score()
        self.check_if_passed()
        self.check_complete()
        if 'update_fields' in kwargs:
            kwargs.pop('update_fields')

        super().save(*args, **kwargs)
        if is_new_instance and self.is_passed:
            self.user.point += 5
            self.user.save()

    def calculate_score(self):
        total_questions = self.quiz.question_set.count()
        correct_answers = self.usersanswer_set.filter(answer__is_right=True).count()
        score = (correct_answers / total_questions) * 100
        self.score = round(score)

    def check_if_passed(self):
        if self.score >= self.quiz.score_required:
            self.is_passed = True
        else:
            self.is_passed = False

    def check_complete(self):
        total_questions = self.quiz.question_set.count()
        total_answers = self.usersanswer_set.filter(answer__isnull=False).count()
        if total_questions == total_answers:
            self.completed = True
        else:
            self.completed = False


class UsersAnswer(models.Model):
    quiz_taker = models.ForeignKey(QuizTaker, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, null=True, blank=True)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)

    def __str__(self):
        return self.question.title













































