from django.db import models
from django.utils.translation import gettext_lazy as _


class Movie(models.Model):
    title = models.CharField(_('title'), max_length=255)
    slug = models.CharField(_('slug'), max_length=255)
    start_release_date = models.DateField(_('start_release'), null=True, blank=True)
    end_release_date = models.DateField(_('end_release'), null=True, blank=True)
    description = models.TextField(_('description'), null=True, blank=True)

    def __str__(self):
        return f'{self.title}'


class Director(models.Model):
    GENDERS = [
        ('m', "Male"),
        ('f', "Female"),
        ('o', "Other"),
    ]

    name = models.CharField(max_length=255)
    movies = models.ForeignKey(Movie, on_delete=models.PROTECT, blank=True, null=True, related_name='director_movies')
    date_of_birth = models.DateField()
    date_of_death = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDERS)
    is_awarded = models.BooleanField(default=False)

    def __str__(self):
        return self.name
