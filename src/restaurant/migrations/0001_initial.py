# Generated by Django 4.1.3 on 2022-11-22 01:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('restaurant_name', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('is_open', models.BooleanField(default=False)),
                ('phone', models.TextField(blank=True, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('email', models.TextField(blank=True, null=True)),
                ('profile', models.ImageField(blank=True, null=True, upload_to='restaurant_profile/')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='restaurant_manager_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
