from django.db import models
from django.utils.translation import gettext_lazy as _


class Movie(models.Model):
    class TypeMovie(models.TextChoices):
        movie = 'movie'
        anime = 'anime'
        tv_series = 'tv_series'

    title = models.CharField(_('title'), max_length=255)
    slug = models.CharField(_('slug'), max_length=255)
    type = models.CharField(max_length=20, choices=TypeMovie.choices, default=TypeMovie.movie)
    start_release_date = models.DateField(_('start_release'), null=True, blank=True)
    end_release_date = models.DateField(_('end_release'), null=True, blank=True)
    description = models.TextField(_('description'), null=True, blank=True)
    director = models.ForeignKey('Director', max_length=255, on_delete=models.CASCADE,
                                 null=True, blank=True, related_name='director_movie')
    imdb_rating = models.FloatField(default=0, null=True, blank=True)
    casts = models.ManyToManyField('Casts', related_name='cast_movies')
    genres = models.ManyToManyField('Genre', related_name='director_movies')
    runtime = models.CharField(_('runtime'), max_length=100, null=True, blank=True)
    episodes = models.PositiveSmallIntegerField(blank=True, null=True)

    def __str__(self):
        return f'{self.title}'


GENDERS = [
    ('m', "Male"),
    ('f', "Female"),
    ('o', "Other"),
]


class Casts(models.Model):
    cast_name = models.CharField(max_length=255)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDERS)
    is_awarded = models.BooleanField(default=False)

    def __str__(self):
        return self.cast_name


class Director(models.Model):

    director_name = models.CharField(max_length=255)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDERS)
    is_awarded = models.BooleanField(default=False)

    def __str__(self):
        return self.director_name


class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


