from django.urls import include, path
from rest_framework import routers

from . import apis
from .apis import RestaurantApiViewset, RestaurantDetailApi

router = routers.SimpleRouter()
router.register('', RestaurantApiViewset, basename='restaurant')

urlpatterns = [
    path('<int:id>', RestaurantDetailApi.as_view()),
    path("create/", apis.RestaurantCreateView.as_view()),
    path("rated", apis.RestaurantMostRatedListApi.as_view()),
    path('', include(router.urls)),
]
