from django.db import models


class Diet(models.Model):
    name = models.TextField()
    description = models.TextField()
    status = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name


class FoodType(models.Model):
    name = models.TextField()
    description = models.TextField()
    status = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name


class Food(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    slug = models.SlugField(null=True, unique=True, blank=True)
    description = models.TextField(null=True, blank=True)
    rating = models.IntegerField(default=0)
    thumbnail = models.ImageField(
        upload_to='food_thumbnail/', null=True, blank=True)
    cover_image = models.ImageField(upload_to='food_cover_image/')
    status = models.BooleanField(default=False)
    createdAt = models.DateField(auto_now=True)
    updatedAt = models.DateField(null=True, blank=True)
    diets = models.ManyToManyField(Diet, blank=True)
    foodTypes = models.ManyToManyField(FoodType, blank=True)
    price = models.FloatField(null=True, blank=True, default=0)
