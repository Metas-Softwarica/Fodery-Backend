import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import *


client = Client()

class LoginRegisterUserTest(TestCase):

    def setUp(self):
        self.user_register_payload = {
            'first_name': 'Sujan',
            'last_name': "Pradhan",
            'email': 'test@gmail.com',
            'password': 'Test12345@'
        }

        self.user_login_payload = {
            'email': 'test@gmail.com',
            'password': 'Test12345@'
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

