from rest_framework.test import APITestCase, APIClient, APIRequestFactory

from accounts.serializers import UserSerializer


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
