from django.urls import path, include
from .apis import RestaurantReviewApiViewset, RestaurantReviewApiDetail, LatestRestaurantReviewApiViewset
from rest_framework import routers

router = routers.SimpleRouter()
router.register('', RestaurantReviewApiViewset, basename='review')
router.register('get-latest', LatestRestaurantReviewApiViewset, basename='get-latest')

urlpatterns = [
    path('<int:id>/', RestaurantReviewApiDetail.as_view()),
    path('', include(router.urls)),
]
