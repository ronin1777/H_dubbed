# import datetime
#
# from django.urls import reverse
# from rest_framework.exceptions import ErrorDetail
# from rest_framework.test import APITestCase, APIClient
#
# from movies.models import Movie
# from movies.serializers import MovieSerializers
#
#
# class MovieSerializersTest(APITestCase):
#     def test_deserialize_valid_movie(self):
#
#         data = {
#             'title': 'Test Movie',
#             'slug': 'test-movie',
#             'start_release_date': '2022-01-01',
#             'end_release_date': '2022-01-31',
#             'description': 'This is a test movie.'
#         }
#         serializer = MovieSerializers(data=data)
#         self.assertTrue(serializer.is_valid())
#         srz_data = serializer.data
#         self.assertEqual(srz_data['title'], 'Test Movie')
#         self.assertEqual(srz_data['slug'], 'test-movie')
#         self.assertEqual(srz_data['start_release_date'], '2022-01-01')
#         self.assertEqual(srz_data['end_release_date'], '2022-01-31')
#         self.assertEqual(srz_data['description'], 'This is a test movie.')
#
#     def test_existing_movie_object(self):
#         data = {
#             'title': 'Test Movie',
#             'slug': 'test-movie',
#         }
#         obj = Movie.objects.create(title='Test Movie', slug='test-movie')
#
#         serializer = MovieSerializers(obj, data=data)
#         self.assertTrue(serializer.is_valid())
#
#         srz_data = serializer.data
#         self.assertEqual(srz_data['title'], 'Test Movie')
#         self.assertEqual(srz_data['description'], None)
#
#     def test_update_existing_movie_object(self):
#         existing_movie = Movie.objects.create(title='Existing Movie', slug='existing-movie')
#         data = {
#             'title': 'Updated Movie',
#             'slug': 'updated-movie',
#             'start_release_date': '2022-01-01',
#             'end_release_date': '2022-01-31',
#             'description': 'This is an updated movie.'
#         }
#         serializer = MovieSerializers(existing_movie, data=data)
#         self.assertTrue(serializer.is_valid())
#         updated_movie = serializer.save()
#         self.assertEqual(updated_movie.title, 'Updated Movie')
#         self.assertEqual(updated_movie.slug, 'updated-movie')
#         self.assertEqual(updated_movie.start_release_date, datetime.date(2022, 1, 1))
#         self.assertEqual(updated_movie.end_release_date, datetime.date(2022, 1, 31))
#         self.assertEqual(updated_movie.description, 'This is an updated movie.')
#
#     def test_handle_invalid_movie_json_missing_fields(self):
#         json_data = {
#             'title': 'Test Movie',
#             'description': 12345
#         }
#         serializer = MovieSerializers(data=json_data)
#         self.assertFalse(serializer.is_valid())
#         self.assertIn('slug', serializer.errors)
#         self.assertEqual(serializer.errors, {'slug': [ErrorDetail(string='This field is required.', code='required')]})
#
#     def test_handle_invalid_movie_json_incorrect_data_types(self):
#         json_data = {
#             'title': 'Test Movie',
#             'slug': 'test-movie',
#             'start_release_date': '1233123',
#             'end_release_date': '2022-01-31',
#         }
#         serializer = MovieSerializers(data=json_data)
#         self.assertFalse(serializer.is_valid())
#         self.assertIn('start_release_date', serializer.errors)


