from django.urls import reverse
from rest_framework.test import APITestCase, APIClient

from movies.models import Movie


class MovieSerializersTest(APITestCase):
    def test_all_movie(self):
        data = {
            'title': 'Test Movie',
            'slug': 'test-movie',
            'type': 'movie',
            'start_release_date': '2022-01-01',
            'end_release_date': '2022-01-31',
            'description': 'This is a test movie.',
            'director': None,
            'imdb_rating': 7.5,
            'casts': [],
            'genres': [],
            'runtime': '120 minutes',
            'episodes': None
        }
        srz = MovieSerializers(data=data)
        self.assertEquals(srz.is_valide)






