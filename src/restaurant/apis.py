from django.db import transaction
from rest_framework import generics, mixins, viewsets
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

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


class RestaurantDetailApi(
    generics.GenericAPIView,
    mixins.RetrieveModelMixin
):
    serializer_class = RestaurantSerializer
    queryset = Restaurant.objects.all()
    permission_classes = (AllowAny,)
    lookup_field = 'id'

    def get(self, request, id):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def get_serializer(self, instance: Restaurant, *args, **kwargs):
        instance.add_view_popularity()
        return super().get_serializer(instance, *args, **kwargs)


class RestaurantMostRatedListApi(generics.ListAPIView):
    pagination_class = None
    queryset = Restaurant.objects.all().order_by('-rating')[:5]
    permission_classes = (AllowAny,)
    serializer_class = RestaurantSerializer
