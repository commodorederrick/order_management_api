# Generated by Django 5.0.7 on 2024-07-17 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_alter_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='delivery_method',
            field=models.CharField(choices=[('standard', 'Standard'), ('express', 'Express'), ('overnight', 'Overnight')], default='standard', max_length=20),
        ),
    ]
