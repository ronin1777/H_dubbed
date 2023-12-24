from unittest import TestCase, mock
from unittest.mock import patch

from rest_framework import status
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.test import APITestCase, APIClient
from django.urls import reverse

from accounts.models import User
from accounts.views import RegisterView


class TestUserRegister(APITestCase):
    def setUp(self):
        self.client = APIClient()

    def test_user_register_valid(self):
        response = self.client.post(reverse('accounts:register'),
                                    data={'email': 'hosein@gmail.com', 'username': 'hosein', 'password': 'hosein123'})
        self.assertEquals(response.status_code, HTTP_201_CREATED)
        self.assertEquals(User.objects.count(), 1)


class TestUserLogin(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='hosein@gmail.com', username='hosein', password='admin123')
        self.client = APIClient()

    def test_login_valid(self):
        response = self.client.post(reverse('users-front:user_login'), data={'username': 'hosein', 'password': 'admin1234'})
        self.assertEquals(response.status_code, 200)
        self.assertIn('access' and 'refresh', response.data)

    def test_login_empty_data(self):
        response = self.client.post(reverse('users-front:user_login'), data={'username': '', 'password': 'admin1234'})
        self.assertEquals(response.data, {"username": ["This field may not be blank."]})
        self.assertNotIn('access' or 'refresh', response.data)


class TestUserLogout(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(email='hosein@gmail.com', username='testuser', password='testpassword')
        self.login_response = self.client.post(reverse('users-front:user_login'), data={'username': 'testuser', 'password': 'testpassword'})
        self.access = self.login_response.data['access']
        self.refresh = self.login_response.data['refresh']
        self.client.credentials(HTTP_AUTHORIZATION='Bear ' + self.access)

    def test_logout(self):

        logout_response = self.client.post(reverse('users-front:user_logout'))
        self.assertEquals(logout_response.status_code, 204)



