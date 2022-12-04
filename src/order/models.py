from django.db import models
from enum import Enum
from datetime import datetime

from src.food.models import FoodInvetory, Extra
from src.user.models import User


class OrderItem(models.Model):
    quantity = models.IntegerField(null=True, blank=True)
    item = models.ForeignKey(
        "Products.Item", on_delete=models.CASCADE, null=True, blank=True)
    variant = models.ForeignKey(
        FoodInvetory, on_delete=models.CASCADE, blank=True, null=True)
    extras = models.ManyToManyField(Extra, blank=True)
    item_price = models.FloatField(default=0, null=True, blank=True)
    extras_price = models.FloatField(default=0, null=True, blank=True)
    total_price = models.FloatField(default=0, null=True, blank=True)


class ExtraOrder(models.Model):
    quantity = models.IntegerField(null=True, blank=True)
    extra = models.ForeignKey(
        Extra, blank=True, on_delete=models.SET_NULL, null=True)


class OrderStatus(Enum):
    pending = 1
    Preparing = 2
    delivering = 3
    delivered = 4


class Order(models.Model):
    billNo = models.IntegerField(default=0)
    note = models.TextField(null=True, blank=True)
    status = models.IntegerField(
        choices=((status.value, status.name) for status in OrderStatus), default=1)
    is_active = models.BooleanField(default=False)
    identifier = models.TextField(null=True, blank=True)
    order_number = models.TextField(null=True, blank=True)
    amount = models.FloatField(null=True, blank=True)
    taxAmount = models.FloatField(null=True, blank=True)
    shipAmount = models.FloatField(null=True, blank=True)
    extraAmount = models.FloatField(null=True, blank=True)
    grandAmount = models.FloatField(null=True, blank=True)
    isPaid = models.BooleanField(default=False, null=True, blank=True)
    isTransactionConfirmed = models.BooleanField(
        default=False, null=True, blank=True)
    extras = models.ManyToManyField(ExtraOrder, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_items = models.ManyToManyField(OrderItem, blank=True)
    created_at = models.DateTimeField(null=True, blank=True, auto_now=True)
    delivered_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateField(null=True, blank=True)

    # def save(self, *args, **kwargs):
    #     if self.identifier == None or self.identifier == "":
    #         self.identifier=bcrypt.hashpw(str(str(self.id)).encode(), bcrypt.gensalt())
    #         generated_key=random_key(8)
    #         flag=False

    #         while not flag:
    #             if Order.objects.filter(order_number=generated_key).exists():
    #                 generated_key=random_key(8)
    #             else:
    #                 self.order_number=generated_key
    #                 flag=True
    #     self.updated_at=datetime.now()
    #     return super().save(*args, **kwargs)
