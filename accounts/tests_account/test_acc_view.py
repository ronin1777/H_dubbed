from unittest import TestCase
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.test import APITestCase, APIClient
from django.urls import reverse

from accounts.models import User


class TestUserRegister(APITestCase):
    def setUp(self):
        self.client = APIClient()

    def test_user_register_valid(self):
        response = self.client.post(reverse('users-front:user_register'),
                                    data={'email': 'hosein@gmail.com', 'username': 'hosein', 'password': 'hosein123'})
        self.assertEquals(response.status_code, HTTP_201_CREATED)
        self.assertEquals(User.objects.count(), 1)
        