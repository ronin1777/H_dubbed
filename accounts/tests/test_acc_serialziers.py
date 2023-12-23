from rest_framework.test import APITestCase, APIClient, APIRequestFactory


class TestRegisterSerializers(APITestCase):
    def test_valid_registration(self):
        data = {'email': 'test@gmail.com', 'username': 'test', 'password': '12345678'}
        serializer = RegisterSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        