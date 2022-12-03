from rest_framework.permissions import AllowAny
from rest_framework import generics, mixins, viewsets
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import Diet, Food, FoodType
from .serializers import DietSerializer, FoodSerializer, FoodTypeSerializer, FoodDetailSerializer


class FoodApiViewset(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Food.objects.all()
    pagination_class = None
    serializer_class = FoodSerializer
    permission_classes = (AllowAny,)
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ('name', 'foodTypes__name', 'diets__name')


class FoodApiDetail(
    generics.GenericAPIView,
    # mixins.ListModelMixin,
    # mixins.CreateModelMixin,
    # mixins.UpdateModelMixin,
    # mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin
):
    serializer_class = FoodDetailSerializer
    pagination_class = None
    queryset = Food.objects.all()
    permission_classes = (AllowAny,)
    lookup_field = 'id'

    def get(self, request, id):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    # def post(self, request):
    #     return self.create(request)

    # def put(self, request, id=None):
    #     return self.update(request, id)

    # def delete(self, request, id=None):
    #     return self.destroy(request, id)


class FoodTypesApiViewset(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = FoodType.objects.all()
    pagination_class = None
    serializer_class = FoodTypeSerializer
    permission_classes = (AllowAny,)
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ('name', 'description', 'status')


class FoodTypesApiDetail(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.RetrieveModelMixin):
    serializer_class = FoodTypeSerializer
    pagination_class = None
    queryset = FoodType.objects.all()
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


class DietsApiViewset(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Diet.objects.all()
    pagination_class = None
    serializer_class = DietSerializer
    permission_classes = (AllowAny,)
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ('name', 'description', 'status')


class DietsApiDetail(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.RetrieveModelMixin):
    serializer_class = DietSerializer
    pagination_class = None
    queryset = Diet.objects.all()
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
