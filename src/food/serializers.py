from rest_framework import serializers
from .models import FoodType, Food, Diet

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'
class FoodTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodType
        fields = ['name', 'description', 'status']
class DietSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diet
        fields = ['name', 'description', 'status']
