from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase


class AuthenticationTest(APITestCase):
    def setUp(self):
        PASSWORD = 'pass1234'
        USERNAME = 'user@example.com'
        self.signup_data = {
            'username': USERNAME,
            'first_name': 'Test',
            'last_name': 'User',
            'password': PASSWORD,
            'confirm_password': PASSWORD,
        }
        self.login_data = {'username': USERNAME, 'password': PASSWORD}

    def create_user(self):
        del self.signup_data['confirm_password']
        return get_user_model().objects.create_user(**self.signup_data)
