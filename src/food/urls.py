from django.urls import path, include
from .views import FoodApiViewset, FoodApiDetail, FoodTypesApiViewset, FoodTypesApiDetail, DietsApiViewset, DietsApiDetail
from rest_framework import routers

router = routers.SimpleRouter()
router.register('', FoodApiViewset, basename='food')
router.register('food-types', FoodTypesApiViewset, basename='food-types')
router.register('diets', DietsApiViewset, basename='diets')

urlpatterns = [
    path('<int:id>/', FoodApiDetail.as_view()),
    path('food-types/<int:id>/', FoodTypesApiDetail.as_view()),
    path('diets/<int:id>/', DietsApiDetail.as_view()),
    path('', include(router.urls)),
]
