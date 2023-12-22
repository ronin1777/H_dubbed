from rest_framework.test import APITestCase, APIClient

from movies.models import Movie
from django.urls import reverse


class MovieViewTest(APITestCase):

    def test_create_movie(self):
        valid_data = {
            'title': 'Test Movie',
            'slug': 'test-movie',
            'start_release_date': '2022-01-01',
            'end_release_date': '2022-01-31',
            'description': 'This is a test movie'
        }
        response = self.client.post('/movie/createmovie/', data=valid_data)

        self.assertEquals(response.status_code, 201)
