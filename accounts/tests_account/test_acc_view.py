from unittest import TestCase, mock
from unittest.mock import patch

from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from rest_framework_simplejwt.tokens import RefreshToken

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
        self.user.is_active = True
        self.user.verified_email = True
        self.user.save()

    def test_login_valid(self):
        data = {'username': 'hosein', 'password': 'admin123'}

        response = self.client.post(reverse('accounts:user_login'), data=data)
        self.assertEquals(response.status_code, 200)
        self.assertIn('access' and 'refresh', response.data)

    def test_login_empty_data(self):
        response = self.client.post(reverse('accounts:user_login'), data={'username': '', 'password': 'admin1234'})
        self.assertEquals(response.data, {"username": ["This field may not be blank."]})
        self.assertNotIn('access' or 'refresh', response.data)




