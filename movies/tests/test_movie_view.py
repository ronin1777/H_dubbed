
from rest_framework import status
from rest_framework.test import APITestCase, APIClient, APIRequestFactory

from accounts.models import User
from movies.models import Movie, Director, Casts, Genre
from django.urls import reverse

from movies.views import MovieCreateView


# class MovieViewTest(APITestCase):
#
#     def test_create_movie(self):
#         valid_data = {
#             'title': 'Test Movie',
#             'slug': 'test-movie',
#             'start_release_date': '2022-01-01',
#             'end_release_date': '2022-01-31',
#             'description': 'This is a test movie'
#         }
#         response = self.client.post('/movie/createmovie/', data=valid_data)
#
#         self.assertEquals(response.status_code, 201)
#
#     def test_filter_movies_by_title(self):
#         Movie.objects.create(title='Test Movie', slug='Test-Movie')
#         response = self.client.get('/movie/createmovie/')
#         self.assertEquals(response.status_code, 200)
#         self.assertEqual(len(response.data), 1)
#
#         first_movie = response.data[0]
#
#         self.assertEqual(first_movie['title'], 'Test Movie')
#         self.assertEqual(first_movie['slug'], 'Test-Movie')
#
#     def test_retrieve_movie_with_valid_id(self):
#         movie = Movie.objects.create(title='Test Movie', slug='test-movie')
#
#         response = self.client.get(f'/movie/updatemovie/{movie.id}/')
#         self.assertEqual(response.status_code, 200)
#
#     def test_search_query(self):
#         Movie.objects.create(title='Test Movie', slug='test-movie')
#         response = self.client.get('/movie/movie_search/')
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(len(response.data), len(Movie.objects.all()))


class MovieCreateViewTest(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.superuser = User.objects.create_superuser(
            username='superuser',
            email='superuser@example.com',
            password='password'
        )
        self.client.force_authenticate(user=self.superuser)

        self.director = Director.objects.create(director_name='Test Director', date_of_birth='1990-01-01', gender='m')
        self.cast = Casts.objects.create(cast_name='Cast', date_of_birth='1995-01-01', gender='f')
        self.genre = Genre.objects.create(name='Genre')

    def test_create_movie_with_valid_data_as_superuser(self):
        data = {
            'title': 'Test movie',
            'slug': 'Test-movie',
            'director': self.director.id,
            'casts': [self.cast.id],
            'genres': [self.genre.id]
        }
        response = self.client.post('/movie/createmovie/', data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'Test movie')







