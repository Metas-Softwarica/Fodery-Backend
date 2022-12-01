from django.urls import path, include

from rest_framework import routers

from . import apis
from .apis import RestaurantApiViewset

router = routers.SimpleRouter()
router.register('', RestaurantApiViewset, basename='restaurant')

urlpatterns = [
    path("create/", apis.RestaurantCreateView.as_view()),
    path('', include(router.urls)),
]