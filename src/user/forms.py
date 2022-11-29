from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from . import models as models


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = models.User
        fields = ('email', )


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = models.User
        fields = ('email',)
