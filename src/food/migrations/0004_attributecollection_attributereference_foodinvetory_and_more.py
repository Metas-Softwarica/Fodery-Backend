# Generated by Django 4.1.3 on 2022-12-12 03:41

from decimal import Decimal
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0003_alter_food_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='AttributeCollection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='AttributeReference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='FoodInvetory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(max_length=20, unique=True)),
                ('is_default', models.BooleanField(default=False)),
                ('retail_price', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))])),
                ('store_price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('attribute_collection', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='attribute_collection_product_inventory', to='food.attributecollection')),
            ],
        ),
        migrations.CreateModel(
            name='VariantPair',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(blank=True, max_length=255, null=True)),
                ('reference', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='attribute_attribute_reference', to='food.attributereference')),
            ],
        ),
        migrations.CreateModel(
            name='VariantPairFoodInventoryPivot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute_pair', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='variant_pair_variant_pair_food_inventory_pivot', to='food.variantpair')),
                ('food_inventory', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='food_inventory_variant_pair_food_inventory_pivot', to='food.foodinvetory')),
            ],
            options={
                'unique_together': {('attribute_pair', 'food_inventory')},
            },
        ),
        migrations.AddField(
            model_name='foodinvetory',
            name='attributes',
            field=models.ManyToManyField(related_name='variant_pair_product_inventory', through='food.VariantPairFoodInventoryPivot', to='food.variantpair'),
        ),
        migrations.AddField(
            model_name='foodinvetory',
            name='food',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='food_food_inventory', to='food.food'),
        ),
        migrations.CreateModel(
            name='AttributeCollectionReferencePivot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute_collection', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='attribute_collection_attribute_collection_reference_pivot', to='food.attributecollection')),
                ('attribute_reference', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='attribute_reference_attribute_collection_reference_pivot', to='food.attributereference')),
            ],
            options={
                'unique_together': {('attribute_reference', 'attribute_collection')},
            },
        ),
        migrations.AddField(
            model_name='attributecollection',
            name='attribute_references',
            field=models.ManyToManyField(related_name='attribute_collection_attribute_reference', through='food.AttributeCollectionReferencePivot', to='food.attributereference'),
        ),
    ]
