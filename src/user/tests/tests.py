from django.test import TestCase

from ..models import *


class ProfileModelTest(TestCase):

    def setUp(self):
        user = User(
            email="test@gmail.com"
        )
        user.save()
        Profile.objects.create(user=user)

    def test_string_representation(self):
        profile = Profile.objects.first()
        self.assertEqual(str(profile), profile.user.email)
