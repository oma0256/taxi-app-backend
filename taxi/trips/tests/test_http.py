from rest_framework import status
from rest_framework.reverse import reverse

from authentication.tests.tests_http import BaseTest
from trips.models import Trip


class HttpTripTest(BaseTest):
    def setUp(self):
        user = self.create_user()
        response = self.login_user(user.username)
        self.access = response.data['access']

    def test_user_can_list_trips(self):
        trips = [
            Trip.objects.create(pick_up_address='A', drop_off_address='B'),
            Trip.objects.create(pick_up_address='B', drop_off_address='C')
        ]
        response = self.client.get(reverse('trip:trip_list'),
            HTTP_AUTHORIZATION=f'Bearer {self.access}'
        )
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        exp_trip_ids = [str(trip.id) for trip in trips]
        act_trip_ids = [trip.get('id') for trip in response.data]
        self.assertCountEqual(exp_trip_ids, act_trip_ids)

    def test_user_can_retrieve_trip_by_id(self):
        trip = Trip.objects.create(pick_up_address='A', drop_off_address='B')
        response = self.client.get(trip.get_absolute_url(),
            HTTP_AUTHORIZATION=f'Bearer {self.access}'
        )
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(str(trip.id), response.data.get('id'))
