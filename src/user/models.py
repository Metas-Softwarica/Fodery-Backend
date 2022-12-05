from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.conf import settings

from src.user.managers import CustomAccountManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("Email Address"), unique=True)
    first_name = models.CharField(max_length=64, null=True, blank=True)
    last_name = models.CharField(max_length=64, null=True, blank=True)
    is_admin = models.BooleanField(default=False)
    is_merchant = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomAccountManager()

    def __str__(self):
        return self.email


class Profile(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='user', on_delete=models.CASCADE, null=True)
    phone = models.TextField(null=True, blank=True)
    birth_date = models.DateField(null=True)
    avatar = models.ImageField(upload_to='avatar/', null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    coverImage = models.ImageField(
        upload_to='coverImage/', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    image_url = models.URLField(null=True, blank=True)
    isPhoneVerified = models.BooleanField(default=False)

    def __str__(self):
        return self.user.email
