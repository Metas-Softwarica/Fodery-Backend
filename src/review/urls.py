from django.urls import include, path
from rest_framework import routers

from .apis import (LatestRestaurantReviewApiViewset, RestaurantReviewApiDetail,
                   RestaurantReviewApiViewset)

router = routers.SimpleRouter()
router.register('', RestaurantReviewApiViewset, basename='review')
router.register('get-latest', LatestRestaurantReviewApiViewset,
                basename='get-latest')

urlpatterns = [
    path('<int:id>/', RestaurantReviewApiDetail.as_view()),
    path('', include(router.urls)),
]
