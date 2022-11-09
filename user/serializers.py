from django.contrib.auth import get_user_model, password_validation
from django.contrib.auth.hashers import check_password
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .validators import validate_password

User = get_user_model()

class RegistrationSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length = 64)
    last_name = serializers.CharField(max_length=64)
    email = serializers.EmailField(
        validators = [UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(
        write_only=True, validators=[validate_password]
    )

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "email",
            "password",
        )

    def create(self, validated_data: dict) -> dict:
        user = User.objects.create_user(
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            email=validated_data["email"],
            password=validated_data["password"],
        )
        return user