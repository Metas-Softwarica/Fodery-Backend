from decimal import Decimal

from django.db import models
from django.core.validators import MinValueValidator


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


class FoodInvetory(models.Model):
    sku = models.CharField(
        max_length=20,
        unique=True,
    )
    food = models.ForeignKey(
        Food, related_name="food_food_inventory", on_delete=models.PROTECT)
    attribute_collection = models.ForeignKey(
        "AttributeCollection", related_name="attribute_collection_product_inventory", on_delete=models.PROTECT, blank=True, null=True,)
    attributes = models.ManyToManyField(
        "VariantPair",
        related_name="variant_pair_product_inventory",
        through="VariantPairFoodInventoryPivot",
    )
    is_default = models.BooleanField(
        default=False,
    )
    retail_price = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal("0.01"))]
    )
    store_price = models.DecimalField(
        max_digits=5,
        decimal_places=2,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return self.sku


class AttributeReference(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class AttributeCollection(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True,
    )
    attribute_references = models.ManyToManyField(
        AttributeReference, related_name="attribute_collection_attribute_reference", through="AttributeCollectionReferencePivot")

    def __str__(self):
        return self.name


class AttributeCollectionReferencePivot(models.Model):
    """
        Pivot Table between Attribute Colleciton and Attribute Reference
    """
    attribute_reference = models.ForeignKey(
        AttributeReference,
        related_name="attribute_reference_attribute_collection_reference_pivot",
        on_delete=models.PROTECT,
    )
    attribute_collection = models.ForeignKey(
        AttributeCollection,
        related_name="attribute_collection_attribute_collection_reference_pivot",
        on_delete=models.PROTECT,
    )

    class Meta:
        unique_together = (("attribute_reference",
                           "attribute_collection"),)


class VariantPair(models.Model):
    reference = models.ForeignKey(
        AttributeReference, related_name="attribute_attribute_reference", on_delete=models.PROTECT)
    value = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.reference.name} : {self.value}"   


class VariantPairFoodInventoryPivot(models.Model):
    """
        Pivot Table between Attribute Pai and Food Inventory
    """
    attribute_pair = models.ForeignKey(
        VariantPair,
        related_name="variant_pair_variant_pair_food_inventory_pivot",
        on_delete=models.PROTECT,
    )
    food_inventory = models.ForeignKey(
        FoodInvetory,
        related_name="food_inventory_variant_pair_food_inventory_pivot",
        on_delete=models.PROTECT,
    )

    class Meta:
        unique_together = (("attribute_pair", "food_inventory"),)
