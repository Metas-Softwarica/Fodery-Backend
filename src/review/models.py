from django.db import models

from src.restaurant.models import Restaurant
from src.user.models import User


class RestaurantReview(models.Model):
    title = models.TextField(blank=True, null=True)
    rating = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    description = models.TextField(null=True, blank=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateField(null=True, blank=True, auto_now=True)
    updated_at = models.DateField(null=True, blank=True)
