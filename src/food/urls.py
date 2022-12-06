from django.urls import include, path
from rest_framework import routers

from .apis import (DietsApiDetail, DietsApiViewset, FoodApiDetail,
                   FoodApiViewset, FoodTypesApiDetail, FoodTypesApiViewset)

router = routers.SimpleRouter()
router.register('', FoodApiViewset, basename='food')
router.register('food-types', FoodTypesApiViewset, basename='food-types')
router.register('diets', DietsApiViewset, basename='diets')

urlpatterns = [
    path('<int:id>', FoodApiDetail.as_view()),
    path('food-types/<int:id>/', FoodTypesApiDetail.as_view()),
    path('diets/<int:id>/', DietsApiDetail.as_view()),
    path('', include(router.urls)),
]
