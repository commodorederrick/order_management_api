# Generated by Django 5.0.7 on 2024-07-17 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_order_delivery_method'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='delivery_provider',
            field=models.CharField(default='jiji', max_length=255),
            preserve_default=False,
        ),
    ]