from django.urls import path, include

from rest_framework_simplejwt import views as jwt_views
from rest_framework_simplejwt.views import TokenObtainPairView

from user import apis

auth_urlpatterns = [
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path(
        "refresh/", jwt_views.TokenRefreshView.as_view(), name="token_refresh"
    ),
    path("register/", apis.RegistrationView.as_view(), name="registration"),
]

urlpatterns = [
    path("auth/", include(auth_urlpatterns)),
]