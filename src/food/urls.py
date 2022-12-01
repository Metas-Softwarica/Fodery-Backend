from django.urls import path, include
from .views import foodApiViewset, foodApiDetail,foodTypesApiViewset, foodTypesApiDetail, dietsApiViewset, dietsApiDetail
from rest_framework import routers

router=routers.SimpleRouter()
router.register('', foodApiViewset, basename='food' )
router.register('food-types', foodTypesApiViewset, basename='food-types' )
router.register('diets', dietsApiViewset, basename='diets' )

urlpatterns = [
    # path('drinks/', genericApiView.as_view()),
    path('<int:id>/', foodApiDetail.as_view()),
    path('food-types/<int:id>/', foodTypesApiDetail.as_view()),
    path('diets/<int:id>/', dietsApiDetail.as_view()),
    path('', include(router.urls)),

    # path('drinks/<int:id>', views.drink_detail)
]
