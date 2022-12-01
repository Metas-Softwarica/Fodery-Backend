from django.db import transaction

from rest_framework import generics, mixins, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import Restaurant
from .serializers import RestaurantSerializer


class RestaurantCreateView(generics.CreateAPIView):
    model = Restaurant
    serializer_class = RestaurantSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        with transaction.atomic():
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            restaurant = serializer.save()
            return Response(
                {
                    "restaurant_name": restaurant.restaurant_name
                }
            )


class RestaurantApiViewset(viewsets.GenericViewSet, mixins.ListModelMixin):
    pagination_class = None
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = (AllowAny,)
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ('restaurant_name', 'address')
