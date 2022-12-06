from rest_framework import serializers

from .models import Diet, Extra, Food, FoodInvetory, FoodType, VariantPair


class RelatedFieldMapperSerializer(serializers.PrimaryKeyRelatedField):
    def __init__(self, **kwargs):
        self.serializer = kwargs.pop('serializer', None)
        if self.serializer is not None and not issubclass(self.serializer, serializers.Serializer):
            raise TypeError('"serializer" is not a valid serializer class')

        super().__init__(**kwargs)

    def use_pk_only_optimization(self):
        return False if self.serializer else True

    def to_representation(self, instance):
        if self.serializer:
            return self.serializer(instance, context=self.context).data
        return super().to_representation(instance)


class ExtraSerializer(serializers.ModelSerializer):

    class Meta:
        model = Extra
        fields = ['id', 'title', 'slug', 'description', 'price', 'cover_image']


class FoodSerializer(serializers.ModelSerializer):
    price = serializers.SerializerMethodField()

    class Meta:
        model = Food
        fields = ['id', 'name', 'slug', 'description',
                  'rating', 'cover_image', 'price', 'popularity']

    def get_price(self, obj: Food):
        queryset = FoodInvetory.objects.filter(
            food=obj).order_by('store_price')
        print(queryset)
        if (queryset.exists()):
            return queryset.first().store_price
        else:
            return None


class FoodDetailSerializer(serializers.ModelSerializer):
    variant = serializers.SerializerMethodField()
    price = serializers.SerializerMethodField()
    extra = ExtraSerializer(many=True)

    class Meta:
        model = Food
        fields = '__all__'

    def get_price(self, obj: Food):
        queryset = FoodInvetory.objects.filter(
            food=obj).order_by('store_price')
        print(queryset)
        if (queryset.exists()):
            return queryset.first().store_price
        else:
            return None

    def get_variant(self, obj: Food):
        queryset = FoodInvetory.objects.filter(
            food=obj).order_by('store_price')
        if (queryset.exists()):
            return FoodInvetorySerializer(queryset, many=True).data
        else:
            return None


class VariantPairSerializer(serializers.ModelSerializer):
    reference = serializers.SerializerMethodField()
    value_id = serializers.IntegerField(source="id", read_only=True)
    reference_id = serializers.SerializerMethodField()

    class Meta:
        model = VariantPair
        fields = ['value_id', 'value', 'reference', 'reference_id']

    def get_reference(self, obj: VariantPair):
        return obj.reference.name

    def get_reference_id(self, obj: VariantPair):
        return obj.reference.id


class FoodInvetorySerializer(serializers.ModelSerializer):
    attributes = VariantPairSerializer(many=True)

    class Meta:
        model = FoodInvetory
        fields = ['sku', 'is_default', 'store_price', 'attributes']
        depth = 2


class FoodTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodType
        fields = ['name', 'description', 'status']


class DietSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diet
        fields = ['name', 'description', 'status']
