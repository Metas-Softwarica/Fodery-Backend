from django.conf import settings
from django.db import models


# Create your models here.
class Restaurant(models.Model):
    restaurant_name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    is_open = models.BooleanField(default=False)
    var_or_tax = models.FloatField(default=0)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, related_name='restaurant_manager_user')
    phone = models.TextField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    email = models.TextField(null=True, blank=True)
    logo = models.ImageField(
        upload_to='restaurant_logo/', null=True, blank=True)
    cover_image = models.ImageField(
        upload_to='restaurant_cover/', null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    rating = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    popularity = models.IntegerField(default=0)

    def add_view_popularity(self):
        self.popularity += 1
        self.save()
