from django.urls import reverse
from rest_framework.test import APITestCase, APIClient

from movies.models import Movie
from movies.serializers import MovieSerializers


class MovieSerializersTest(APITestCase):
    def test_all_movie(self):

        data = {
            'title': 'Test Movie',
            'slug': 'test-movie',
            'start_release_date': '2022-01-01',
            'end_release_date': '2022-01-31',
            'description': 'This is a test movie.'
        }
        serializer = MovieSerializers(data=data)
        self.assertTrue(serializer.is_valid())
        srz_data = serializer.data
        self.assertEqual(srz_data['title'], 'Test Movie')
        self.assertEqual(srz_data['slug'], 'test-movie')
        self.assertEqual(srz_data['start_release_date'], '2022-01-01')
        self.assertEqual(srz_data['end_release_date'], '2022-01-31')
        self.assertEqual(srz_data['description'], 'This is a test movie.')





