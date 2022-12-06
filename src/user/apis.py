import json
import os

import google_apis_oauth
import requests
from django.contrib.auth import login
from django.contrib.auth.models import Group
from django.db import transaction
from django.http.response import HttpResponse, HttpResponseBadRequest
from django.shortcuts import HttpResponseRedirect
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView

from config import settings

from .models import Profile, User
from .serializers import (AdminTokenObtainPairSerializer,
                          DeliveryTokenObtainPairSerializer,
                          RegistrationSerializer,
                          RestaurantManagerTokenObtainPairSerializer)
from .services import token


class RegistrationView(generics.CreateAPIView):
    model = User
    serializer_class = RegistrationSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        with transaction.atomic():
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.save()


class AdminRegistrationView(generics.CreateAPIView):
    model = User
    serializer_class = RegistrationSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        with transaction.atomic():
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.save()
            group = Group.objects.get(name="Admin")
            user.groups.add(group)


class DeliveryRegistrationView(generics.CreateAPIView):
    model = User
    serializer_class = RegistrationSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        with transaction.atomic():
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.save()
            group = Group.objects.get(name="Delivery")
            user.groups.add(group)


class RestaurantManagerRegistrationView(generics.CreateAPIView):
    model = User
    serializer_class = RegistrationSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        with transaction.atomic():
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.save()
            group = Group.objects.get(name="RestaurantManager")
            user.groups.add(group)


class AdminTokenObtainPairView(TokenObtainPairView):
    serializer_class = AdminTokenObtainPairSerializer


class DeliveryTokenObtainPairView(TokenObtainPairView):
    serializer_class = DeliveryTokenObtainPairSerializer


class RestaurantManagerTokenObtainPairView(TokenObtainPairView):
    serializer_class = RestaurantManagerTokenObtainPairSerializer


# The url where the google oauth should redirect after a successful login.
REDIRECT_URI = 'http://backend.sweedapp.com/user/google/callback/'
# REDIRECT_URI = 'exp://192.168.1.73:19000'

# Authorization scopes required
SCOPES = ['https://www.googleapis.com/auth/userinfo.profile',
          'https://www.googleapis.com/auth/userinfo.email', "openid"]

JSON_FILEPATH = os.path.join(os.getcwd(), 'client9.json')


def RedirectGoogleSignin(request):
    oauth_url = google_apis_oauth.get_authorization_url(
        JSON_FILEPATH, SCOPES, REDIRECT_URI)
    return HttpResponseRedirect(oauth_url)


def CallbackGoogleSignin(request):
    try:
        credentials = google_apis_oauth.get_crendentials_from_callback(
            request,
            JSON_FILEPATH,
            SCOPES,
            REDIRECT_URI
        )
        stringified_token = google_apis_oauth.stringify_credentials(
            credentials)
        stringified_token = json.loads(stringified_token)
        response = requests.get(
            f"https://www.googleapis.com/oauth2/v3/userinfo?access_token={stringified_token['token']}")
        jsonData = response.json()
        print(jsonData)
        if jsonData['email']:
            userData = {
                "first_name": jsonData['given_name'],
                "last_name": jsonData['family_name']
            }
            user, userExist = User.objects.get_or_create(
                email=jsonData["email"])
            profile.__dict__.update(userData)
            user.save()
            profile, _ = Profile.objects.get_or_create(user=user)
            profile.save()
            user.backend = settings.AUTH_PASSWORD_VALIDATORS[0]['NAME']
            login(request, user)
            # HttpResponseRedirect.allowed_schemes.append('sweed')
            token_payload = token.get_tokens_for_user(user=user)
            print(token_payload)
            # return HttpResponseRedirect(f"sweed://?access_token={access_token}&refresh_token={refresh_token}")
            return HttpResponse(token)
        return HttpResponseBadRequest("Login Failed")
    except google_apis_oauth.InvalidLoginException:
        return HttpResponseBadRequest("Login Failed")
