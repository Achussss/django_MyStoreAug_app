# Generated by Django 4.1.3 on 2023-01-12 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='carts',
            name='status',
            field=models.CharField(choices=[('order-placed', 'order-placed'), ('in-cart', 'in-cart'), ('cancelled', 'cancelled')], default='in-cart', max_length=200),
        ),
    ]
