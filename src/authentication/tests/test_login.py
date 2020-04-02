import base64
import json

from rest_framework import status
from rest_framework.reverse import reverse

from .base import AuthenticationTest


class LoginTest(AuthenticationTest):
    def test_user_can_log_in(self):
        user = self.create_user()
        response = self.client.post(reverse('login'), data=self.login_data)

        access = response.data['access']
        header, payload, signature = access.split('.')
        decoded_payload = base64.b64decode(f'{payload}==')
        payload_data = json.loads(decoded_payload)

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertIsNotNone(response.data['refresh'])
        self.assertEqual(payload_data['id'], user.id)
        self.assertEqual(payload_data['username'], user.username)
        self.assertEqual(payload_data['first_name'], user.first_name)
        self.assertEqual(payload_data['last_name'], user.last_name)
