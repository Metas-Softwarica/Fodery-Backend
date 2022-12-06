from rest_framework import serializers

from .models import RestaurantReview


class RestaurantReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantReview
        fields = '__all__'
