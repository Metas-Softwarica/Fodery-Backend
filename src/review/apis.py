from rest_framework import generics, mixins, viewsets
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import AllowAny

from .models import RestaurantReview
from .serializers import RestaurantReviewSerializer


class RestaurantReviewApiViewset(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = RestaurantReview.objects.all()
    pagination_class = None
    serializer_class = RestaurantReviewSerializer
    permission_classes = (AllowAny,)
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ('rating', 'user__name', 'restaurant__name')


class LatestRestaurantReviewApiViewset(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = RestaurantReview.objects.all().order_by('-created_at')[:5]
    pagination_class = None
    serializer_class = RestaurantReviewSerializer
    permission_classes = (AllowAny,)
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ('created_at', 'user__name', 'restaurant__name')

# class MyRestaurantReviewApiViewset(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
#     queryset = RestaurantReview.objects.filter(user=request.user.id)
#     pagination_class = None
#     serializer_class = RestaurantReviewSerializer
#     permission_classes = (AllowAny,)
#     filter_backends = [SearchFilter, OrderingFilter]
#     search_fields = ('created_at', 'user__name', 'restaurant__name')


class RestaurantReviewApiDetail(
    generics.GenericAPIView,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin
):
    serializer_class = RestaurantReviewSerializer
    pagination_class = None
    queryset = RestaurantReview.objects.all()
    permission_classes = (AllowAny,)
    lookup_field = 'id'

    def get(self, request, id):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id=None):
        return self.destroy(request, id)


# class FoodTypesApiViewset(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
#     queryset = FoodType.objects.all()
#     pagination_class = None
#     serializer_class = FoodTypeSerializer
#     permission_classes = (AllowAny,)
#     filter_backends = [SearchFilter, OrderingFilter]
#     search_fields = ('name', 'description', 'status')


# class FoodTypesApiDetail(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.RetrieveModelMixin):
#     serializer_class = FoodTypeSerializer
#     pagination_class = None
#     queryset = FoodType.objects.all()
#     permission_classes = (AllowAny,)
#     lookup_field = 'id'

#     def get(self, request, id):
#         if id:
#             return self.retrieve(request)
#         else:
#             return self.list(request)

#     def post(self, request):
#         return self.create(request)

#     def put(self, request, id=None):
#         return self.update(request, id)

#     def delete(self, request, id=None):
#         return self.destroy(request, id)


# class DietsApiViewset(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
#     queryset = Diet.objects.all()
#     pagination_class = None
#     serializer_class = DietSerializer
#     permission_classes = (AllowAny,)
#     filter_backends = [SearchFilter, OrderingFilter]
#     search_fields = ('name', 'description', 'status')


# class DietsApiDetail(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.RetrieveModelMixin):
#     serializer_class = DietSerializer
#     pagination_class = None
#     queryset = Diet.objects.all()
#     permission_classes = (AllowAny,)
#     lookup_field = 'id'

#     def get(self, request, id):
#         if id:
#             return self.retrieve(request)
#         else:
#             return self.list(request)

#     def post(self, request):
#         return self.create(request)

#     def put(self, request, id=None):
#         return self.update(request, id)

#     def delete(self, request, id=None):
#         return self.destroy(request, id)
