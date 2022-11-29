from django.db import models

# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    slug = models.SlugField(null=True, unique=True,blank=True)
    description = models.TextField(null=True, blank=True)
    rating = models.IntegerField(default=0)
    thumbnail = models.ImageField(upload_to='food_thumbnail/', null=True, blank=True)
    cover_image = models.ImageField(upload_to='food_cover_image/')
    status = models.BooleanField(default=False)
    createdAt = models.DateField(auto_now=True)
    updatedAt = models.DateField(null=True, blank=True)