from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from accounts.models import User


class ProfileCreateTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(username='usertest', email='usertest@example.com', password='testpassword')
        self.client.force_authenticate(user=self.user)

    def test_create_profile(self):

        profile_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'gender': 'M',
            'age': 30,
            'birthday': '2023-10-04',
            'phone_number': '09123456789',
            'bio': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
        }
        response = self.client.post('http://127.0.0.1/Profile/', data=profile_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)



