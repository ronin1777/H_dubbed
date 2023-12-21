from django.test import TestCase
from ..models import Movie


class ModelMovieTest(TestCase):
    def test_model_exist(self):
        obj = Movie.objects.count()
        self.assertEquals(obj, 0)
