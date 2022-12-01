import json

from django.test import TestCase, Client
from django.urls import reverse

from rest_framework import status

from ..models import *


client = Client()


class LoginRegisterUserTest(TestCase):
    def setUp(self):
        self.user_register_payload = {
            'restaurant_name': 'Test Restaurant',
            'description': "This is the description.",
            'var_or_tax': '13',
            'phone': '9876543210',
            'address': 'Nepal',
            'email': 'test@restaurant.com'
        }
        
    def test_register_and_login_user(self):
        response = client.post(reverse('registration'),
                               data=json.dumps(self.user_register_payload),
                               content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = client.post(reverse('token_obtain_pair'),
                               data=json.dumps(self.user_login_payload),
                               content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
