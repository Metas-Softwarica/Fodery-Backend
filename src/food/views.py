from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Food
from.serializers import FoodSerializer
from django.http import JsonResponse
from rest_framework import status
# Create your views here.
from .serializers import FoodSerializer, FoodTypeSerializer, DietSerializer
from .models import Food, FoodType, Diet
from rest_framework.permissions import AllowAny


from rest_framework import generics, mixins, viewsets
from rest_framework.authentication import TokenAuthentication 
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter

# get all foods and create api

class foodApiViewset(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    permission_classes = (AllowAny,)
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ('name', 'foodTypes__name', 'diets__name')


 # get food via id with CRUD api
class foodApiDetail(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.RetrieveModelMixin):

    serializer_class = FoodSerializer
    queryset = Food.objects.all()
    permission_classes = (AllowAny,)

    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
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


# FOOD TYPE
# get all FoodTypes api

class foodTypesApiViewset(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = FoodType.objects.all()
    serializer_class = FoodTypeSerializer
    permission_classes = (AllowAny,)
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ('name', 'description','status')


# get foodTypes via id API with CRUD
class foodTypesApiDetail(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.RetrieveModelMixin):

    serializer_class = FoodTypeSerializer
    queryset = FoodType.objects.all()
    permission_classes = (AllowAny,)

    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
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

# // DIET 
# get all and create API 
class dietsApiViewset(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Diet.objects.all()
    serializer_class = DietSerializer
    permission_classes = (AllowAny,)
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ('name', 'description','status')


# get diet via id API with CRUD
class dietsApiDetail(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.RetrieveModelMixin):

    serializer_class = DietSerializer
    queryset = Diet.objects.all()
    permission_classes = (AllowAny,)

    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
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



