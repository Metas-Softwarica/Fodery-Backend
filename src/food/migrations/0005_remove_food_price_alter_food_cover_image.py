# Generated by Django 4.1.3 on 2022-12-12 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0004_attributecollection_attributereference_foodinvetory_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='food',
            name='price',
        ),
        migrations.AlterField(
            model_name='food',
            name='cover_image',
            field=models.ImageField(blank=True, null=True, upload_to='food_cover_image/'),
        ),
    ]
