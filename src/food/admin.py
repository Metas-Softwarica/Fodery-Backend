from django.contrib import admin
from .models import Food, FoodType, Diet, VariantPair, AttributeCollection, AttributeCollectionReferencePivot, FoodInvetory, AttributeReference, VariantPairFoodInventoryPivot, Extra


admin.site.register(Food)
admin.site.register(FoodType)
admin.site.register(Diet)
admin.site.register(VariantPair)
admin.site.register(AttributeCollection)
admin.site.register(AttributeCollectionReferencePivot)
admin.site.register(FoodInvetory)
admin.site.register(AttributeReference)
admin.site.register(VariantPairFoodInventoryPivot)
admin.site.register(Extra)
