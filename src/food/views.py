from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Food
from.serializers import FoodSerializer
from django.http import JsonResponse
from rest_framework import status
# Create your views here.
from .serializers import FoodSerializer, FoodTypeSerializer, DietSerializer
from .models import Food
from rest_framework.permissions import AllowAny


from rest_framework import generics, mixins, viewsets
from rest_framework.authentication import TokenAuthentication 
from rest_framework.permissions import IsAuthenticated


# get all
class foodApiViewset(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = FoodSerializer
    queryset = Food.objects.all()
    permission_classes = (AllowAny,)


  
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



