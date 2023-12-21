from rest_framework.test import APITestCase, APIClient

from movies.models import Movie
from django.urls import reverse


class MovieViewTest(APITestCase):

    def setUp(self):
        client = APIClient

    def test_create_movie(self):
        data = {
            'title': 'Test Movie',
            'slug': 'test-movie',
        }
        response = self.client.post(path='movie:cl_movie', data=data)

        self.assertEquals(response.status_code, 201)
