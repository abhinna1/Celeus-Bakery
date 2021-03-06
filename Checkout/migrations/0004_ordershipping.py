# Generated by Django 3.2.5 on 2022-02-18 14:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Basket', '0008_alter_itembasket_basket_id'),
        ('Checkout', '0003_rename_order_shippinginfo_basket'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderShipping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('basket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Basket.basket')),
                ('shippingInfo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Checkout.shippinginfo')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
