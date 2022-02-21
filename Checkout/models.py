from django.db import models
from Basket.models import Basket
from Register.models import User

# Create your models here.
class ShippingInfo (models.Model):
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=10, null=True, blank=True)
    order_date = models.DateField(null=True)
    is_delivered = models.BooleanField(default=False)

    def __str__(self):
        return str(self.address)


class OrderShipping (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE)
    shippingInfo = models.ForeignKey(ShippingInfo, on_delete=models.CASCADE)
    delivered = models.BooleanField(default=False)
    def __str__(self):
        return str(self.user)