from django.db import models


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


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    
    def __str__(self):
        return self.title


















































