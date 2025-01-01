# Generated by Django 5.1.4 on 2024-12-31 01:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cuisine', '0001_initial'),
        ('order', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='ordercuisine',
            name='cuisine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cuisine.cuisine'),
        ),
        migrations.AddField(
            model_name='ordercuisine',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.order'),
        ),
        migrations.AddField(
            model_name='order',
            name='cuisines',
            field=models.ManyToManyField(through='order.OrderCuisine', to='cuisine.cuisine'),
        ),
    ]