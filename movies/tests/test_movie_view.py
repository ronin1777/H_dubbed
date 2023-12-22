from rest_framework.test import APITestCase, APIClient, APIRequestFactory

from movies.models import Movie
from django.urls import reverse

from movies.views import MovieCreateView


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

    def test_filter_movies_by_title(self):
        Movie.objects.create(title='Test Movie', slug='Test-Movie')
        response = self.client.get('/movie/createmovie/')
        self.assertEquals(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

        first_movie = response.data[0]

        self.assertEqual(first_movie['title'], 'Test Movie')
        self.assertEqual(first_movie['slug'], 'Test-Movie')

    def test_retrieve_movie_with_valid_id(self):
        movie = Movie.objects.create(title='Test Movie', slug='test-movie')

        response = self.client.get(f'/movie/updatemovie/{movie.id}/')
        self.assertEqual(response.status_code, 200)





