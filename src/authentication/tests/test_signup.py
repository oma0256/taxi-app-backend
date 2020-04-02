from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.reverse import reverse

from .base import AuthenticationTest


class SignupTest(AuthenticationTest):
    def test_user_can_sign_up(self):
        response = self.client.post(reverse('signup'), data=self.signup_data)
        user = get_user_model().objects.last()
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(response.data['id'], user.id)
        self.assertEqual(response.data['username'], user.username)
        self.assertEqual(response.data['first_name'], user.first_name)
        self.assertEqual(response.data['last_name'], user.last_name)
