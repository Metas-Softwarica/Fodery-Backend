# Generated by Django 4.1.3 on 2022-12-12 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0006_extra_food_extra'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extra',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
