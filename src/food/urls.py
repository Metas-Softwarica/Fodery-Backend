from django.urls import path, include
from .views import foodApiViewset, foodApiDetail
from rest_framework import routers

router=routers.SimpleRouter()
router.register('', foodApiViewset, basename='food' )

urlpatterns = [
    # path('drinks/', genericApiView.as_view()),
    path('<int:id>/', foodApiDetail.as_view()),
    path('', include(router.urls)),

    # path('drinks/<int:id>', views.drink_detail)
]
