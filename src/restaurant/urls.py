from django.urls import path, include

from . import apis


urlpatterns = [
    path("create/", apis.RestaurantCreateView.as_view()),
    path("list", apis.RestaurantListView.as_view()),
]