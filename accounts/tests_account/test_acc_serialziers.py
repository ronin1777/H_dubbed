import unittest

from rest_framework.test import APITestCase, APIClient, APIRequestFactory

from accounts.models import User
from accounts.serializers import UserSerializer, LogInSerializer, EmailVerificationSerializer


class TestRegisterSerializers(APITestCase):
    def test_valid_registration(self):
        data = {'email': 'test@gmail.com', 'username': 'test', 'password': '12345678'}
        serializer = UserSerializer(data=data)
        self.assertTrue(serializer.is_valid())

        validate_data = serializer.validated_data
        self.assertEquals(validate_data['email'], 'test@gmail.com')
        self.assertEqual(validate_data['username'], 'test')
        self.assertEqual(validate_data['password'], '12345678')

    def test_invalid_registration(self):

        data = {'email': 'test@example.com', 'username': 'test@gmail.com', 'password': 'test'}
        serializer = UserSerializer(data=data)
        self.assertEqual(serializer.is_valid(), False)
        self.assertEqual(serializer.errors['password'], ['Ensure this field has at least 8 characters.'])

    def test_invalid_email(self):
        data = {'email': 'invalid_email', 'username': 'test', 'password': '12345678'}
        serializer = UserSerializer(data=data)
        self.assertEqual(serializer.is_valid(), False)
        self.assertEqual(serializer.errors['email'], ['Enter a valid email address.'])

    class LogInSerializerTestCase(unittest.TestCase):
        def test_get_tokens(self):
            user = User.objects.create_user(username='111testone', email='111testone@email.com', password='1123456789')
            serializer = LogInSerializer()
            data = {
                'username': '111testone',
                'email': '111testone@email.com',
                'password': '1123456789'
            }
            tokens = serializer.validate(data)

            self.assertIn('access', tokens)
            self.assertIn('refresh', tokens)
            self.assertIsInstance(tokens['access'], str)
            self.assertIsInstance(tokens['refresh'], str)

        def test_valid_user_with_valid_token(self):
            user = User(token='valid_token')
            serializer = EmailVerificationSerializer(user)
            expected_data = {'token': 'valid_token'}
            self.assertEqual(serializer.data, expected_data)
