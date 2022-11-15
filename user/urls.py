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
admin_urlpatterns = [
    path('login/', apis.AdminTokenObtainPairView.as_view(), name="admin_login"),
    path("register/", apis.AdminRegistrationView.as_view(), name="registration"),
]

restaurant_manager_urlpatterns = [
    path('login/', apis.RestaurantManagerTokenObtainPairView.as_view(),
         name="rmanager_login"),
    path("register/", apis.RestaurantManagerRegistrationView.as_view(),
         name="registration"),
]

delivery_urlpatterns = [
    path('login/', apis.DeliveryTokenObtainPairView.as_view(), name="delivery_login"),
    path("register/", apis.DeliveryRegistrationView.as_view(), name="registration"),
]

urlpatterns = [
    path("auth/", include(auth_urlpatterns)),
    path("admin/auth/", include(admin_urlpatterns)),
    path("rmanager/auth/", include(restaurant_manager_urlpatterns)),
    path("delivery/auth/", include(delivery_urlpatterns)),
]
