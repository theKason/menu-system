# Generated by Django 3.1.12 on 2024-12-14 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_auto_20241212_0427'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]