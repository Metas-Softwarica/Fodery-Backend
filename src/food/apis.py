# from django.db import transaction

# from rest_framework import generics
# from rest_framework.permissions import AllowAny
# from rest_framework.response import Response

# from .models import Food
# from .serializers import FoodSerializer

# class FoodCreateView(generics.CreateAPIView):
#     model = Food
#     serializer_class = FoodSerializer
#     permission_classes = (AllowAny,)

#     def post(self, request, *args, **kwargs):
#         with transaction.atomic():
#             serializer = self.get_serializer(data=request.data)
#             serializer.is_valid(raise_exception=True)
#             restaurant = serializer.save()
#             return Response(
#                 {
#                     "restaurant_name": restaurant.restaurant_name
#                 }
#             )

# class RestaurantListView(generics.ListAPIView):
#     pagination_class = None
#     queryset = Restaurant.objects.filter()
#     permission_classes = (AllowAny,)
#     serializer_class = RestaurantSerializer